from enum import Enum


class CardSuit(Enum):
    """Enum representing different card shape types and their face counts."""
    BLACK_CLUBS = 1
    RED_DIAMONDS = 2
    RED_HEARTS = 3
    BLACK_SPADES = 4

    def __eq__(self, other):
        if not isinstance(other, CardSuit):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, CardSuit):
            return NotImplemented
        return self.value < other.value

    def __gt__(self, other):
        if not isinstance(other, CardSuit):
            return NotImplemented
        return self.value > other.value


class CardRank(Enum):
    """Enum representing different card level types and their face counts."""
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def __eq__(self, other):
        if not isinstance(other, CardRank):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, CardRank):
            return NotImplemented
        return self.value < other.value

    def __gt__(self, other):
        if not isinstance(other, CardRank):
            return NotImplemented
        return self.value > other.value
