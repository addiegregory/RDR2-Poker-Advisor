from advisor import PokerAdvisor
from card_parser import parse_cards, validate_unique_cards
from hand_evaluator import HandEvaluator
from probability import ProbabilitySimulator


def get_cards(prompt, valid_counts):
    """ Request cards until the user enters a valid amount """
    while True:
        try:
            cards = parse_cards(input(prompt))

            if len(cards) not in valid_counts:
                allowed = ", ".join(str(count) for count in valid_counts)
                print(f"Please enter one of these card counts: {allowed}")
                continue

            return cards

        except ValueError as error:
            print(f"Error: {error}")


def get_integer(prompt, minimum, maximum):
    """ Request an integer within a specified range """
    while True:
        try:
            value = int(input(prompt))

            if value < minimum or value > maximum:
                print(f"Enter a number from {minimum} to {maximum}.")
                continue

            return value

        except ValueError:
            print("Please enter a whole number.")


def get_float(prompt, minimum=0.0, allow_equal=True):
    """ Request a decimal value at or above a minimum """
    while True:
        try:
            value = float(input(prompt))

            if allow_equal and value < minimum:
                print(f"Enter a value of at least {minimum}.")
                continue

            if not allow_equal and value <= minimum:
                print(f"Enter a value greater than {minimum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def display_cards(cards):
    """ Return a readable list of cards """
    return ", ".join(str(card) for card in cards)


def main():
    print("=" * 50)
    print("RDR2 Poker Advisor")
    print("=" * 50)
    print("Enter cards using codes such as AS, KH, 10C, or QD.")
    print()

    player_cards = get_cards(
        "Enter your two cards: ",
        (2,)
    )

    while True:
        community_cards = get_cards(
            "Enter community cards "
            "(leave blank pre-flop, or enter 3, 4, or 5): ",
            (0, 3, 4, 5)
        )

        try:
            validate_unique_cards(player_cards + community_cards)
            break
        except ValueError as error:
            print(f"Error: {error}")

    num_opponents = get_integer(
        "Enter the number of active opponents (1-5): ",
        1,
        5
    )

    pot = get_float("Enter the current pot: $")
    cost_to_call = get_float("Enter the amount required to call: $")
    player_stack = get_float(
        "Enter your remaining money at the table: $",
        minimum=0.0,
        allow_equal=False
    )

    simulation_text = input(
        "Number of simulations [press Enter for 5000]: "
    ).strip()

    if simulation_text:
        try:
            simulations = int(simulation_text)

            if simulations <= 0:
                raise ValueError

        except ValueError:
            print("Invalid simulation count. Using 5000.")
            simulations = 5000
    else:
        simulations = 5000

    print()
    print("Analyzing the current hand...")

    # A made hand can be displayed after at least three community cards.
    if len(player_cards + community_cards) >= 5:
        current_result = HandEvaluator.evaluate_hand(
            player_cards + community_cards
        )

        print(f"Current hand: {current_result['name']}")
        print(
            "Best five cards: "
            f"{display_cards(current_result['cards'])}"
        )
    else:
        print("Current hand: Pre-flop starting hand")

    probabilities = ProbabilitySimulator.estimate_equity(
        player_cards,
        community_cards,
        num_opponents,
        simulations
    )

    recommendation = PokerAdvisor.recommend(
        probabilities["equity"],
        pot,
        cost_to_call,
        player_stack
    )

    print()
    print("-" * 50)
    print(f"Player cards: {display_cards(player_cards)}")

    if community_cards:
        print(f"Community cards: {display_cards(community_cards)}")
    else:
        print("Community cards: None")

    print(f"Opponents: {num_opponents}")
    print(f"Simulations: {probabilities['simulations']:,}")
    print(
        f"Win probability: "
        f"{probabilities['win_probability']:.1%}"
    )
    print(
        f"Tie probability: "
        f"{probabilities['tie_probability']:.1%}"
    )
    print(f"Estimated equity: {probabilities['equity']:.1%}")
    print(
        f"Required equity: "
        f"{recommendation['required_equity']:.1%}"
    )
    print()
    print(f"Recommendation: {recommendation['action']}")
    print(f"Confidence: {recommendation['confidence']}")
    print(f"Reason: {recommendation['reason']}")
    print("-" * 50)


if __name__ == "__main__":
    main()