from abc import ABC, abstractmethod


class Handler(ABC):
    """
    Abstract base class for the Chain of Responsibility pattern.
    Each handler decides whether to handle the operation or pass
    it along to the next handler in the chain.
    """

    def __init__(self):
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @abstractmethod
    def handle(self, numbers):
        pass
