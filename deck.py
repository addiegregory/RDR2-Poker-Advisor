import random
from card import Card


class Deck:
    """ Represents standard 54-card deck """

    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        """ Restore deck to original 52 cards """
        self.cards.clear()

        for suit in Card.VALID_SUITS:
            for rank in Card.VALID_RANKS:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        """ Randomize remaining unknown cards """
        random.shuffle(self.cards)

    def deal(self):
        """ Remove and return one card from deck """
        if len(self.cards) == 0:
            raise IndexError("Cannot deal from an empty deck")

        return self.cards.pop()

    def remove_card(self, rank, suit):
        """ Remove card already visible in RDR2 poker hand """
        for card in self.cards:
            if card.rank == rank and card.suit == suit:
                self.cards.remove(card)
                return card

        raise ValueError(f"{rank} of {suit} is not available in the deck")

    def __len__(self):
        return len(self.cards)