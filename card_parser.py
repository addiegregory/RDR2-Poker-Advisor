from card import Card


SUIT_CODES = {
    "H": "Hearts",
    "D": "Diamonds",
    "C": "Clubs",
    "S": "Spades"
}


def validate_unique_cards(cards):
    """ Raise an error if the same card appears more than once """
    card_pairs = [(card.rank, card.suit) for card in cards]

    if len(card_pairs) != len(set(card_pairs)):
        raise ValueError("Duplicate cards are not allowed")


def parse_card(card_text):
    """ Convert compact input such as AS or 10H into a Card """
    card_text = card_text.strip().upper()

    if len(card_text) < 2:
        raise ValueError(f"Invalid card: {card_text}")

    rank = card_text[:-1]
    suit_code = card_text[-1]

    if suit_code not in SUIT_CODES:
        raise ValueError(f"Invalid suit code: {suit_code}")

    suit = SUIT_CODES[suit_code]

    return Card(rank, suit)


def parse_cards(cards_text):
    """ Convert space-separated card codes into Card objects """
    if not cards_text.strip():
        return []

    card_codes = cards_text.split()
    cards = [parse_card(code) for code in card_codes]

    validate_unique_cards(cards)

    return cards