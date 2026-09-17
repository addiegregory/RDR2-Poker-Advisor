
class Card:
    """ Represents a standard playing card. """

    VALID_RANKS = (
        "2", "3", "4", "5", "6", "7", "8",
        "9", "10", "J", "Q", "K", "A"
    )
    
    VALID_SUITS = (
        "Hearts",
        "Diamonds",
        "Clubs",
        "Spades"
    )

    RANK_VALUES = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }

    def __init__(self, rank: str, suit: str):
        if rank not in Card.VALID_RANKS:
            raise ValueError(f"Invalid rank: {rank}")

        if suit not in Card.VALID_SUITS:
            raise ValueError(f"Invalid suit: {suit}")

        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def get_value(self) -> int:
        return Card.RANK_VALUES[self.rank]

    def __lt__(self, other: "Card") -> bool:
        return self.get_value() < other.get_value()