# RDR2-Poker-Advisor

A Python command-line application that analyzes Texas Hold'em situations in *Red Dead Redemption 2*. The advisor evaluates the player's cards, estimates equity through Monte Carlo simulation, compares that equity with pot odds, and recommends whether to check, call, raise, or fold.

## Project Status

Version 1.0.0 is the first complete command-line release. Users can manually enter an RDR2 poker situation and receive a probability-based recommendation with an explanation.

## Current Features

- Accepts compact card input such as `AS`, `KH`, and `10C`
- Simulates unknown opponent and community cards
- Estimates win, tie, loss, and equity percentages
- Calculates pot odds and required equity
- Considers the number of opponents and the player's remaining money
- Recommends checking, calling, raising, or folding
- Explains the reasoning behind each recommendation

## Card Input

Enter cards using the rank followed by the first letter of the suit:

```text
AS  = Ace of Spades
KH  = King of Hearts
10C = Ten of Clubs
QD  = Queen of Diamonds
```

Separate multiple cards with spaces:

```text
AS KH
```

## Example Output

```text
Current hand: One Pair
Win probability: 48.2%
Tie probability: 2.1%
Estimated equity: 49.0%
Required equity: 25.0%

Recommendation: Call
Confidence: Moderate
Reason: Your estimated equity is greater than the equity required to call.
```

Results may vary slightly because unknown cards are generated randomly during each simulation.

## How It Works

1. Removes the player and community cards from a virtual 52-card deck.
2. Generates possible opponent hands and remaining community cards.
3. Evaluates and compares every completed hand.
4. Repeats the process thousands of times to estimate the player's equity.
5. Compares the estimated equity with the pot odds to recommend an action.

## Current Limitations

Opponent cards are currently modeled as uniformly random. Version 1.0.0 does not yet account for individual NPC betting patterns, table position, previous actions, or different opponent play styles.

## Running the Program

From the project folder, run:

```bash
py main.py
```
To test, run:
```bash
py -m unittest discover -s tests
```

## Releases

### v1.0.0 - Interactive Poker Advisor

Added manual game input, Monte Carlo equity simulation, pot-odds calculations, stack-aware recommendations, explanations, and expanded automated testing.
### v0.3.0 - Hand Evaluator

Added a Texas Hold'em hand-evaluation engine that identifies every standard hand type and selects the strongest five-card hand from five to seven available cards.

### v0.2.0 - Deck System

Added the internal deck system used to track known and unknown cards during poker analysis, along with automated tests.

### v0.1.0 - Initial Release

Added card representation, validation, readable display, numerical rank values, and rank comparison.

## Disclaimer

This is an independent educational project and is not affiliated with or endorsed by Rockstar Games or Take-Two Interactive.