import unittest

from card_parser import parse_cards
from probability import ProbabilitySimulator


class TestProbabilitySimulator(unittest.TestCase):

    def test_probabilities_total_one(self):
        result = ProbabilitySimulator.estimate_equity(
            parse_cards("AS KH"),
            parse_cards("QS JC 4D"),
            num_opponents=2,
            simulations=100
        )

        total = (
            result["win_probability"]
            + result["tie_probability"]
            + result["loss_probability"]
        )

        self.assertAlmostEqual(total, 1.0)


    def test_player_royal_flush_always_wins(self):
        result = ProbabilitySimulator.estimate_equity(
            parse_cards("AS KS"),
            parse_cards("QS JS 10S 4D 2C"),
            num_opponents=2,
            simulations=50
        )

        self.assertEqual(result["win_probability"], 1.0)
        self.assertEqual(result["equity"], 1.0)


    def test_royal_flush_board_always_ties(self):
        result = ProbabilitySimulator.estimate_equity(
            parse_cards("2C 3D"),
            parse_cards("AS KS QS JS 10S"),
            num_opponents=1,
            simulations=50
        )

        self.assertEqual(result["tie_probability"], 1.0)
        self.assertEqual(result["equity"], 0.5)


    def test_invalid_player_card_count(self):
        with self.assertRaises(ValueError):
            ProbabilitySimulator.estimate_equity(
                parse_cards("AS"),
                [],
                num_opponents=1,
                simulations=10
            )


    def test_invalid_community_card_count(self):
        with self.assertRaises(ValueError):
            ProbabilitySimulator.estimate_equity(
                parse_cards("AS KH"),
                parse_cards("QS JS"),
                num_opponents=1,
                simulations=10
            )


    def test_invalid_opponent_count(self):
        with self.assertRaises(ValueError):
            ProbabilitySimulator.estimate_equity(
                parse_cards("AS KH"),
                [],
                num_opponents=0,
                simulations=10
            )


if __name__ == "__main__":
    unittest.main()