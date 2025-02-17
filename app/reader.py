from abc import abstractmethod
from typing import Protocol


class Reader(Protocol):

    @abstractmethod
    def read(self) -> str: ...


class IOReader(Reader):
    def read(self) -> str:
        try:
            user_input: str = input("> ")
        except (EOFError, KeyboardInterrupt):
            raise
        return user_input
