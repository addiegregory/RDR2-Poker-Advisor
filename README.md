# RDR2-Poker-Advisor

A Python command-line application that analyzes Texas Hold'em situations in *Red Dead Redemption 2*. The advisor evaluates the player's cards, estimates equity through Monte Carlo simulation, compares that equity with pot odds, and recommends whether to check, call, raise, or fold.

## Project Status

Version 1.0.0 is the first complete command-line release. Users can manually enter an RDR2 poker situation and receive a probability-based recommendation with an explanation.

## In Development
Screenshot-based card recognition using computer vision. The advisor will identify player and community cards directly from RDR2 gameplay.

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

## How It Works

1. Removes the player and community cards from a virtual 52-card deck.
2. Generates possible opponent hands and remaining community cards.
3. Evaluates and compares every completed hand.
4. Repeats the process thousands of times to estimate the player's equity.
5. Compares the estimated equity with the pot odds to recommend an action.

## Current Limitations

Opponent cards are currently modeled as uniformly random. Version 1.0.0 does not yet account for individual NPC betting patterns, table position, previous actions, or different opponent play styles.

Computer-vision support is currently experimental and not included in the stable v1.0.0 release.

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

See the [GitHub Releases](https://github.com/addiegregory/RDR2-Poker-Advisor/releases) page for version history and release notes.

Current stable release: **v1.0.0 - Interactive Poker Advisor**
## Disclaimer

This is an independent educational project and is not affiliated with or endorsed by Rockstar Games or Take-Two Interactive.
