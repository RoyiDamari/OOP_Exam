from enums import CardRank, CardSuit


class Card:
    """
    Represents a playing card with a suit, rank, and face state.
    The card's suit and rank are read-only.
    """

    def __init__(self, suit: CardSuit, rank: CardRank, face_up=True):
        self.__suit = suit
        self.__rank = rank
        self.__face_up = face_up

    @property
    def suit(self):
        return self.__suit

    @property
    def rank(self):
        return self.__rank

    @property
    def face_up(self):
        return self.__face_up

    def flip(self):
        self.__face_up = not self.__face_up
        return self.__face_up

    def get_display_name(self):
        return f"{self.rank.name} OF {self.suit.name}"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank < other.rank

    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        if self.rank == other.rank:
            return self.suit > other.suit
        return self.rank > other.rank

    def __hash__(self):
        """Returns the hash code based on the card number and it's type."""
        return hash((self.rank, self.suit))

    def __str__(self):
        if self.face_up:
            return self.get_display_name()
        return "?"

    def __repr__(self):
        return f"('{self.suit}', '{self.rank}', {self.face_up})"