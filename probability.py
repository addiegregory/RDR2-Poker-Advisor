from deck import Deck
from hand_evaluator import HandEvaluator
from card_parser import validate_unique_cards


class ProbabilitySimulator:
    """ Estimates poker equity through randomized simulations """

    @staticmethod
    def estimate_equity(
        player_cards,
        community_cards,
        num_opponents,
        simulations=5000
    ):
        """ Estimate the player's equity against unknown opponents """
        if len(player_cards) != 2:
            raise ValueError("Exactly two player cards are required")

        if len(community_cards) not in (0, 3, 4, 5):
            raise ValueError(
                "Community cards must contain 0, 3, 4, or 5 cards"
            )

        if num_opponents < 1 or num_opponents > 5:
            raise ValueError("The number of opponents must be between 1 and 5")

        if simulations <= 0:
            raise ValueError("The number of simulations must be positive")

        known_cards = player_cards + community_cards
        validate_unique_cards(known_cards)

        wins = 0
        ties = 0
        losses = 0
        equity_total = 0.0

        for _ in range(simulations):
            deck = Deck()

            # Remove every card currently visible in RDR2.
            for card in known_cards:
                deck.remove_card(card.rank, card.suit)

            deck.shuffle()

            # Generate hypothetical cards for each opponent.
            opponent_hands = []

            for _ in range(num_opponents):
                opponent_hands.append([
                    deck.draw_unknown_card(),
                    deck.draw_unknown_card()
                ])

            # Generate any community cards that have not appeared yet.
            simulated_community = list(community_cards)

            while len(simulated_community) < 5:
                simulated_community.append(deck.draw_unknown_card())

            player_result = HandEvaluator.evaluate_hand(
                player_cards + simulated_community
            )
            player_score = player_result["score"]

            opponent_scores = []

            for opponent_hand in opponent_hands:
                opponent_result = HandEvaluator.evaluate_hand(
                    opponent_hand + simulated_community
                )
                opponent_scores.append(opponent_result["score"])

            all_scores = [player_score] + opponent_scores
            best_score = max(all_scores)
            number_of_winners = all_scores.count(best_score)

            if player_score == best_score:
                if number_of_winners == 1:
                    wins += 1
                else:
                    ties += 1

                # Split equity when multiple players tie.
                equity_total += 1 / number_of_winners
            else:
                losses += 1

        return {
            "wins": wins,
            "ties": ties,
            "losses": losses,
            "win_probability": wins / simulations,
            "tie_probability": ties / simulations,
            "loss_probability": losses / simulations,
            "equity": equity_total / simulations,
            "simulations": simulations
        }