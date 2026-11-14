import unittest

from card_parser import parse_card, parse_cards


class TestCardParser(unittest.TestCase):

    def test_parse_ace_of_spades(self):
        card = parse_card("AS")

        self.assertEqual(card.rank, "A")
        self.assertEqual(card.suit, "Spades")


    def test_parse_ten_of_clubs(self):
        card = parse_card("10C")

        self.assertEqual(card.rank, "10")
        self.assertEqual(card.suit, "Clubs")


    def test_lowercase_input(self):
        card = parse_card("qh")

        self.assertEqual(card.rank, "Q")
        self.assertEqual(card.suit, "Hearts")


    def test_parse_multiple_cards(self):
        cards = parse_cards("AS KH 10C")

        self.assertEqual(len(cards), 3)
        self.assertEqual(str(cards[0]), "A of Spades")


    def test_empty_input(self):
        self.assertEqual(parse_cards(""), [])


    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            parse_card("20S")


    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            parse_card("AX")


    def test_duplicate_cards(self):
        with self.assertRaises(ValueError):
            parse_cards("AS KH AS")


if __name__ == "__main__":
    unittest.main()