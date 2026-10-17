import unittest
from card import Card


class TestCard(unittest.TestCase):

    def test_create_valid_card(self):
        card = Card("A", "Spades")

        self.assertEqual(card.rank, "A")
        self.assertEqual(card.suit, "Spades")

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            Card("20", "Spades")

    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            Card("A", "Stars")

    def test_card_display(self):
        card = Card("K", "Hearts")

        self.assertEqual(str(card), "K of Hearts")

    def test_rank_value(self):
        card = Card("Q", "Diamonds")

        self.assertEqual(card.get_value(), 12)

    def test_card_comparison(self):
        queen = Card("Q", "Hearts")
        ace = Card("A", "Spades")

        self.assertTrue(queen < ace)
        self.assertFalse(ace < queen)


if __name__ == "__main__":
    unittest.main()