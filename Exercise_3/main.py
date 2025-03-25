from deck import Deck
from card import Card
from enums import CardRank, CardSuit
from custom_errors import DeckCheatingError, DoubleSameCardError


def main():
    ace_of_spades = Card(CardSuit.BLACK_SPADES, CardRank.KING)
    king_of_hearts = Card(CardSuit.RED_HEARTS, CardRank.KING)

    print(f"First card: {ace_of_spades}")
    print(f"Second card: {king_of_hearts}")

    if ace_of_spades > king_of_hearts:
        print(f"{ace_of_spades} is higher than {king_of_hearts}")

    # first time flipping the card down
    ace_of_spades.flip()
    print(f"After flipping: {ace_of_spades}")

    deck = Deck()
    print(f"Deck size: {len(deck)}")

    # Check of two random equal shuffles
    try:
        new_deck = deck.shuffle()
        print("New deck size after shuffling:", len(new_deck))
    except DeckCheatingError as e:
        print(f"{e}")

    # Check of adding double same card
    try:
        deck.add_card(ace_of_spades)
    except DoubleSameCardError as e:
        print(f"{e}")

    # Draw a card from the top
    drawn_card = deck.draw()
    print("Card drawn from the deck:", drawn_card)
    print("Deck size after drawing a card:", len(deck))

    # Add the drawn card back to the bottom of the deck
    deck.add_card(drawn_card)
    print("Deck size after adding the drawn card back to the bottom:", len(deck))

    # second time flipping the card up
    ace_of_spades.flip()
    print(f"After flipping: {ace_of_spades}")

    # Iterate over the deck
    print("\nAccessing cards directly by index:")
    for i in range(5):
        print(f"Card at index {i}: {deck[i]}")

    # Iterate over the deck
    print("\nIterating through all cards in the deck:")
    for card in deck:
        print(card)


if __name__ == "__main__":
    main()
