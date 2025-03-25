class DeckCheatingError(ValueError):
    """Raised when both shuffles return the exact same deck (same order of cards)."""

    def __init__(self, message="Cheating detected! Deck not shuffled properly!"):
        super().__init__(message)


class DoubleSameCardError(ValueError):
    """Raised when trying to add a card that already exist in the deck."""

    def __init__(self, message="This card is already in the deck and cannot be added."):
        super().__init__(message)
