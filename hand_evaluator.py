from itertools import combinations

class HandEvaluator:
    """ Evaluates and compares poker hands """

    HAND_NAMES = {
        0: "High Card",
        1: "One Pair",
        2: "Two Pair",
        3: "Three of a Kind",
        4: "Straight",
        5: "Flush",
        6: "Full House",
        7: "Four of a Kind",
        8: "Straight Flush"
    }

    @staticmethod
    def count_ranks(cards):
        """ Count how many times each card rank appears """
        rank_counts = {}

        for card in cards:
            value = card.get_value()

            if value in rank_counts:
                rank_counts[value] += 1
            else:
                rank_counts[value] = 1

        return rank_counts

    @staticmethod
    def get_straight_high(cards):
        """ Return highest straight card, or None if there is no straight """
        values = sorted({card.get_value() for card in cards})

        if len(values) != 5:
            return None

        # An ace can act as 1 in an A-2-3-4-5 straight.
        if values == [2, 3, 4, 5, 14]:
            return 5

        if values[-1] - values[0] == 4:
            return values[-1]

        return None

    @staticmethod
    def is_flush(cards):
        """ Return True when all five cards have same suit """
        suits = {card.suit for card in cards}

        return len(suits) == 1

    @staticmethod
    def score_five_cards(cards):
        """ Return a tuple representing strength of a five-card hand """
        if len(cards) != 5:
            raise ValueError("Exactly five cards are required")

        rank_counts = HandEvaluator.count_ranks(cards)
        straight_high = HandEvaluator.get_straight_high(cards)
        flush = HandEvaluator.is_flush(cards)

        pairs = []
        three_of_a_kind = []
        four_of_a_kind = []

        # Group ranks based on how many times they appear
        for rank, count in rank_counts.items():
            if count == 2:
                pairs.append(rank)
            elif count == 3:
                three_of_a_kind.append(rank)
            elif count == 4:
                four_of_a_kind.append(rank)

        # Higher ranks considered before lower ranks
        pairs.sort(reverse=True)
        three_of_a_kind.sort(reverse=True)
        four_of_a_kind.sort(reverse=True)

        all_ranks = sorted(rank_counts.keys(), reverse=True)

        # Check each hand from strongest to weakest
        if straight_high is not None and flush:
            return 8, straight_high

        if four_of_a_kind:
            four_rank = four_of_a_kind[0]
            kicker = max(
                rank for rank in all_ranks if rank != four_rank
            )
            return 7, four_rank, kicker

        if three_of_a_kind and pairs:
            return 6, three_of_a_kind[0], pairs[0]

        if flush:
            return 5, *all_ranks

        if straight_high is not None:
            return 4, straight_high

        if three_of_a_kind:
            three_rank = three_of_a_kind[0]
            kickers = sorted(
                (rank for rank in all_ranks if rank != three_rank),
                reverse=True
            )
            return 3, three_rank, *kickers

        if len(pairs) == 2:
            high_pair = pairs[0]
            low_pair = pairs[1]
            kicker = max(
                rank for rank in all_ranks if rank not in pairs
            )
            return 2, high_pair, low_pair, kicker

        if len(pairs) == 1:
            pair_rank = pairs[0]
            kickers = sorted(
                (rank for rank in all_ranks if rank != pair_rank),
                reverse=True
            )
            return 1, pair_rank, *kickers

        # If no ranks repeat, score the hand using its cards in descending order.
        return 0, *all_ranks

    @staticmethod
    def evaluate_hand(cards):
        """ Find and return the strongest five-card poker hand """
        if len(cards) < 5 or len(cards) > 7:
            raise ValueError("A poker hand evaluation requires 5 to 7 cards")

        # Check that the same physical card was not entered twice.
        card_pairs = [(card.rank, card.suit) for card in cards]

        if len(card_pairs) != len(set(card_pairs)):
            raise ValueError("Duplicate cards are not allowed")

        best_score = None
        best_cards = None

        # Evaluate every possible five-card combination
        for five_cards in combinations(cards, 5):
            score = HandEvaluator.score_five_cards(five_cards)

            if best_score is None or score > best_score:
                best_score = score
                best_cards = five_cards

        if best_score is None or best_cards is None:
            raise ValueError("Unable to evaluate the provided cards")

        if best_score == (8, 14):
            hand_name = "Royal Flush"
        else:
            hand_name = HandEvaluator.HAND_NAMES[best_score[0]]

        return {
            "name": hand_name,
            "score": best_score,
            "cards": list(best_cards)
        }