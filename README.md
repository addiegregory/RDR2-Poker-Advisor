# RDR2-Poker-Advisor

A Python application designed to analyze Texas Hold'em situations in Red Dead Redemption 2. The completed advisor will evaluate the player's cards, estimate win probability, compare that probability with pot odds, and recommend whether to check, call, raise, or fold.

## Project Status

This project is currently in early development. Version 0.2.0 establishes the card and deck systems needed for future hand evaluation and probability simulations.

## Current Features

- Models and validates standard playing cards
- Tracks known and unknown cards using a 52-card deck
- Draws hypothetical unknown cards for future probability simulations
- Identifies all standard Texas Hold'em hand types
- Handles kickers, tie comparisons, and ace-low straights
- Rejects duplicate cards and invalid hand sizes
- Includes automated tests for card, deck, and hand-evalution behavior


## Running the program

From the project folder, run:

```
py main.py
```
To test, run:
```
py -m unittest discover -s tests
```

## Releases

### v0.3.0 - Hand Evaluator

Added a Texas Hold'em hand-evaluation engine that identifies every standard hand type and selects the strongest five-card hand from five to seven available cards.

### v0.2.0 - Deck System

Added the internal deck system used to track known and unknown cards during poker analysis, along with automated tests.

### v0.1.0 - Initial Release

Added card representation, validation, readable display, numerical rank values, and rank comparison.

## Disclaimer

This is an independent educational project and is not affiliated with or endorsed by Rockstar Games or Take-Two Interactive.