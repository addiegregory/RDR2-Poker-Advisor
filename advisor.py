class PokerAdvisor:
    """ Produces rule-based recommendations using equity and pot odds """

    @staticmethod
    def calculate_required_equity(pot, cost_to_call):
        """ Calculate the equity needed for a profitable call """
        if pot < 0:
            raise ValueError("The pot cannot be negative")

        if cost_to_call < 0:
            raise ValueError("The cost to call cannot be negative")

        if cost_to_call == 0:
            return 0.0

        return cost_to_call / (pot + cost_to_call)


    @staticmethod
    def recommend(equity, pot, cost_to_call, player_stack):
        """ Recommend checking, calling, raising, or folding """
        if equity < 0 or equity > 1:
            raise ValueError("Equity must be between 0 and 1")

        if player_stack <= 0:
            raise ValueError("Player stack must be greater than zero")

        if cost_to_call < 0:
            raise ValueError("The cost to call cannot be negative")

        effective_call = min(cost_to_call, player_stack)
        required_equity = PokerAdvisor.calculate_required_equity(
            pot,
            effective_call
        )

        equity_advantage = equity - required_equity
        all_in_call = cost_to_call >= player_stack and cost_to_call > 0

        # No opponent bet needs to be matched.
        if cost_to_call == 0:
            if equity >= 0.65:
                return {
                    "action": "Raise",
                    "confidence": "High",
                    "required_equity": 0.0,
                    "equity_advantage": equity,
                    "reason": (
                        "No call is required and your estimated equity "
                        "is strong enough to bet for value."
                    )
                }

            return {
                "action": "Check",
                "confidence": "Moderate",
                "required_equity": 0.0,
                "equity_advantage": equity,
                "reason": (
                    "Checking costs nothing and keeps you in the hand "
                    "without committing more money."
                )
            }

        # Calling is not supported by the estimated equity.
        if equity < required_equity:
            return {
                "action": "Fold",
                "confidence": "High",
                "required_equity": required_equity,
                "equity_advantage": equity_advantage,
                "reason": (
                    "Your estimated equity is lower than the equity "
                    "required to call this bet."
                )
            }

        # Strong hands may benefit from raising for additional value.
        if equity >= 0.70 and not all_in_call:
            return {
                "action": "Raise",
                "confidence": "High",
                "required_equity": required_equity,
                "equity_advantage": equity_advantage,
                "reason": (
                    "Your estimated equity is substantially higher than "
                    "the amount required to continue."
                )
            }

        if all_in_call:
            return {
                "action": "Call All-In",
                "confidence": "Moderate",
                "required_equity": required_equity,
                "equity_advantage": equity_advantage,
                "reason": (
                    "Your estimated equity supports calling, but the call "
                    "requires your remaining stack."
                )
            }

        return {
            "action": "Call",
            "confidence": "Moderate",
            "required_equity": required_equity,
            "equity_advantage": equity_advantage,
            "reason": (
                "Your estimated equity is greater than the equity "
                "required to call."
            )
        }