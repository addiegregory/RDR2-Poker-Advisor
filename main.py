from card import Card


def main():

    ace = Card("A", "Spades")
    queen = Card("Q", "Hearts")

    print(f"Card: {ace}")
    print(f"Value: {ace.get_value()}")

    print(f"Card: {queen}")
    print(f"Value: {queen.get_value()}")

    print(f"Is {ace} higher than {queen}? {ace > queen}")

if __name__ == "__main__":
    main()