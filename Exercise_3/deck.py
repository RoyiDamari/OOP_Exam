from enums import CardSuit, CardRank
from card import Card
import random
from custom_errors import DeckCheatingError, DoubleSameCardError
from typing import List


def fair_deck(func):
    """Decorator for a random shaffle of the deck and for checking that the order of the cards in each deck is not similar."""

    def wrapper(*args, **kwargs):

        self_instance = args[0]
        print("Starting shuffling...")
        original_order = self_instance.cards

        first_shaffle = func(*args, **kwargs)

        second_shaffle = original_order.copy()
        random.shuffle(second_shaffle)

        if first_shaffle == second_shaffle:
            raise DeckCheatingError()
        else:
            print("Deck created and shuffled:")
            return first_shaffle

    return wrapper


class Deck:
    """
    Represents a deck of 52 cards.
    Supports shuffling, drawing, adding cards, and iteration.
    """

    def __init__(self, shuffle_flag: bool = True):
        self.shuffle_flag = shuffle_flag
        self.__cards: List[Card] = [Card(suit, rank) for suit in CardSuit for rank in CardRank]

        if self.shuffle_flag:
            self.shuffle()

    @property
    def cards(self):
        return self.__cards.copy()

    @fair_deck
    def shuffle(self):
        random.shuffle(self.__cards)
        return self.cards

    def draw(self):
        if self.__cards:
            return self.__cards.pop(0)
        return None # for clarification

    def add_card(self, card: Card):
        if card in self.__cards:
            raise DoubleSameCardError
        self.__cards.append(card)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        try:
            return self.cards[index]
        except IndexError as e:
            print(f"error={e}")
            return None # for clarification

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.__cards):
            raise StopIteration
        value = self.__cards[self._index]
        self._index += 1
        return value
