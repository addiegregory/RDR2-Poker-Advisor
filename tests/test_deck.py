import unittest
from card import Card
from deck import Deck


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_deck_contains_52_cards(self):
        self.assertEqual(len(self.deck), 52)

    def test_all_cards_are_unique(self):
        card_pairs = []

        for card in self.deck.cards:
            card_pairs.append((card.rank, card.suit))

        self.assertEqual(len(card_pairs), len(set(card_pairs)))

    def test_remove_known_card(self):
        removed_card = self.deck.remove_card("A", "Spades")

        self.assertEqual(removed_card.rank, "A")
        self.assertEqual(removed_card.suit, "Spades")
        self.assertEqual(len(self.deck), 51)

    def test_card_cannot_be_removed_twice(self):
        self.deck.remove_card("A", "Spades")

        with self.assertRaises(ValueError):
            self.deck.remove_card("A", "Spades")

    def test_draw_unknown_card(self):
        drawn_card = self.deck.deal()

        self.assertIsInstance(drawn_card, Card)
        self.assertEqual(len(self.deck), 51)

    def test_reset_restores_deck(self):
        self.deck.remove_card("A", "Spades")
        self.deck.deal()
        self.deck.reset()

        self.assertEqual(len(self.deck), 52)

    def test_draw_from_empty_deck(self):
        for _ in range(52):
            self.deck.deal()

        with self.assertRaises(IndexError):
            self.deck.deal()

    def test_shuffle_preserves_cards(self):
        cards_before = {
            (card.rank, card.suit) for card in self.deck.cards
        }

        self.deck.shuffle()

        cards_after = {
            (card.rank, card.suit) for card in self.deck.cards
        }

        self.assertEqual(cards_before, cards_after)
        self.assertEqual(len(self.deck), 52)


if __name__ == "__main__":
    unittest.main()