import unittest
from card import Card
from hand_evaluator import HandEvaluator


class TestHandEvaluator(unittest.TestCase):

    def test_count_ranks_with_pair(self):
        cards = [
            Card("A", "Spades"),
            Card("A", "Hearts"),
            Card("10", "Clubs"),
            Card("7", "Diamonds"),
            Card("2", "Spades")
        ]

        counts = HandEvaluator.count_ranks(cards)

        self.assertEqual(counts[14], 2)
        self.assertEqual(counts[10], 1)
        self.assertEqual(counts[7], 1)
        self.assertEqual(counts[2], 1)

    def test_invalid_hand_size(self):
        cards = [
            Card("A", "Spades"),
            Card("K", "Hearts"),
            Card("Q", "Clubs"),
            Card("J", "Diamonds")
        ]

        with self.assertRaises(ValueError):
            HandEvaluator.score_five_cards(cards)

    def test_high_card(self):
        cards = [
            Card("A", "Spades"),
            Card("J", "Hearts"),
            Card("8", "Clubs"),
            Card("5", "Diamonds"),
            Card("2", "Spades")
        ]

        score = HandEvaluator.score_five_cards(cards)

        self.assertEqual(score, (0, 14, 11, 8, 5, 2))

    def test_one_pair(self):
        cards = [
            Card("A", "Spades"),
            Card("A", "Hearts"),
            Card("10", "Clubs"),
            Card("7", "Diamonds"),
            Card("2", "Spades")
        ]

        score = HandEvaluator.score_five_cards(cards)

        self.assertEqual(score, (1, 14, 10, 7, 2))

    def test_two_pair(self):
        cards = [
            Card("K", "Spades"),
            Card("K", "Hearts"),
            Card("8", "Clubs"),
            Card("8", "Diamonds"),
            Card("A", "Spades")
        ]

        score = HandEvaluator.score_five_cards(cards)

        self.assertEqual(score, (2, 13, 8, 14))

    def test_three_of_a_kind(self):
        cards = [
            Card("Q", "Spades"),
            Card("Q", "Hearts"),
            Card("Q", "Clubs"),
            Card("9", "Diamonds"),
            Card("4", "Spades")
        ]

        score = HandEvaluator.score_five_cards(cards)

        self.assertEqual(score, (3, 12, 9, 4))

    def test_straight(self):
        cards = [
            Card("10", "Spades"),
            Card("J", "Hearts"),
            Card("Q", "Clubs"),
            Card("K", "Diamonds"),
            Card("A", "Spades")
        ]

        score = HandEvaluator.score_five_cards(cards)

        self.assertEqual(score, (4, 14))

    def test_ace_low_straight(self):
        cards = [
            Card("A", "Spades"),
            Card("2", "Hearts"),
            Card("3", "Clubs"),
            Card("4", "Diamonds"),
            Card("5", "Spades")
        ]

        score = HandEvaluator.score_five_cards(cards)

        self.assertEqual(score, (4, 5))

    def test_flush(self):
        cards = [
            Card("A", "Hearts"),
            Card("J", "Hearts"),
            Card("8", "Hearts"),
            Card("5", "Hearts"),
            Card("2", "Hearts")
        ]

        score = HandEvaluator.score_five_cards(cards)

        self.assertEqual(score, (5, 14, 11, 8, 5, 2))

    def test_full_house(self):
        cards = [
            Card("J", "Spades"),
            Card("J", "Hearts"),
            Card("J", "Clubs"),
            Card("6", "Diamonds"),
            Card("6", "Spades")
        ]

        score = HandEvaluator.score_five_cards(cards)

        self.assertEqual(score, (6, 11, 6))

    def test_four_of_a_kind(self):
        cards = [
            Card("9", "Spades"),
            Card("9", "Hearts"),
            Card("9", "Clubs"),
            Card("9", "Diamonds"),
            Card("A", "Spades")
        ]

        score = HandEvaluator.score_five_cards(cards)

        self.assertEqual(score, (7, 9, 14))

    def test_straight_flush(self):
        cards = [
            Card("5", "Spades"),
            Card("6", "Spades"),
            Card("7", "Spades"),
            Card("8", "Spades"),
            Card("9", "Spades")
        ]

        score = HandEvaluator.score_five_cards(cards)

        self.assertEqual(score, (8, 9))

    def test_royal_flush(self):
        cards = [
            Card("10", "Diamonds"),
            Card("J", "Diamonds"),
            Card("Q", "Diamonds"),
            Card("K", "Diamonds"),
            Card("A", "Diamonds")
        ]

        score = HandEvaluator.score_five_cards(cards)

        self.assertEqual(score, (8, 14))

    def test_higher_pair_has_higher_score(self):
        pair_of_aces = [
            Card("A", "Spades"),
            Card("A", "Hearts"),
            Card("10", "Clubs"),
            Card("7", "Diamonds"),
            Card("2", "Spades")
        ]

        pair_of_kings = [
            Card("K", "Spades"),
            Card("K", "Hearts"),
            Card("10", "Diamonds"),
            Card("7", "Clubs"),
            Card("2", "Hearts")
        ]

        ace_score = HandEvaluator.score_five_cards(pair_of_aces)
        king_score = HandEvaluator.score_five_cards(pair_of_kings)

        self.assertGreater(ace_score, king_score)

    def test_best_hand_from_seven_cards(self):
        cards = [
            Card("A", "Spades"),
            Card("K", "Spades"),
            Card("Q", "Spades"),
            Card("J", "Spades"),
            Card("10", "Spades"),
            Card("4", "Diamonds"),
            Card("2", "Clubs")
        ]

        result = HandEvaluator.evaluate_hand(cards)

        self.assertEqual(result["name"], "Royal Flush")
        self.assertEqual(result["score"], (8, 14))
        self.assertEqual(len(result["cards"]), 5)

    def test_best_hand_selects_full_house(self):
        cards = [
            Card("K", "Spades"),
            Card("K", "Hearts"),
            Card("K", "Clubs"),
            Card("8", "Spades"),
            Card("8", "Hearts"),
            Card("3", "Diamonds"),
            Card("2", "Clubs")
        ]

        result = HandEvaluator.evaluate_hand(cards)

        self.assertEqual(result["name"], "Full House")
        self.assertEqual(result["score"], (6, 13, 8))

    def test_duplicate_cards_are_rejected(self):
        cards = [
            Card("A", "Spades"),
            Card("A", "Spades"),
            Card("K", "Hearts"),
            Card("Q", "Clubs"),
            Card("J", "Diamonds")
        ]

        with self.assertRaises(ValueError):
            HandEvaluator.evaluate_hand(cards)

    def test_too_few_cards_are_rejected(self):
        cards = [
            Card("A", "Spades"),
            Card("K", "Hearts"),
            Card("Q", "Clubs"),
            Card("J", "Diamonds")
        ]

        with self.assertRaises(ValueError):
            HandEvaluator.evaluate_hand(cards)

    def test_too_many_cards_are_rejected(self):
        cards = [
            Card("A", "Spades"),
            Card("K", "Hearts"),
            Card("Q", "Clubs"),
            Card("J", "Diamonds"),
            Card("10", "Spades"),
            Card("9", "Hearts"),
            Card("8", "Clubs"),
            Card("7", "Diamonds")
        ]

        with self.assertRaises(ValueError):
            HandEvaluator.evaluate_hand(cards)


if __name__ == "__main__":
    unittest.main()