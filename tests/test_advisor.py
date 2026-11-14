import unittest

from advisor import PokerAdvisor


class TestPokerAdvisor(unittest.TestCase):

    def test_required_equity(self):
        required = PokerAdvisor.calculate_required_equity(6.0, 2.0)

        self.assertEqual(required, 0.25)


    def test_fold_recommendation(self):
        result = PokerAdvisor.recommend(
            equity=0.10,
            pot=6.0,
            cost_to_call=2.0,
            player_stack=10.0
        )

        self.assertEqual(result["action"], "Fold")


    def test_call_recommendation(self):
        result = PokerAdvisor.recommend(
            equity=0.50,
            pot=6.0,
            cost_to_call=2.0,
            player_stack=10.0
        )

        self.assertEqual(result["action"], "Call")


    def test_raise_recommendation(self):
        result = PokerAdvisor.recommend(
            equity=0.80,
            pot=6.0,
            cost_to_call=2.0,
            player_stack=10.0
        )

        self.assertEqual(result["action"], "Raise")


    def test_check_recommendation(self):
        result = PokerAdvisor.recommend(
            equity=0.40,
            pot=6.0,
            cost_to_call=0.0,
            player_stack=10.0
        )

        self.assertEqual(result["action"], "Check")


    def test_raise_when_checking_is_available(self):
        result = PokerAdvisor.recommend(
            equity=0.75,
            pot=6.0,
            cost_to_call=0.0,
            player_stack=10.0
        )

        self.assertEqual(result["action"], "Raise")


    def test_all_in_call(self):
        result = PokerAdvisor.recommend(
            equity=0.60,
            pot=10.0,
            cost_to_call=5.0,
            player_stack=5.0
        )

        self.assertEqual(result["action"], "Call All-In")


if __name__ == "__main__":
    unittest.main()