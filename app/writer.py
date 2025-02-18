from abc import abstractmethod
from typing import Protocol


class Writer(Protocol):
    @abstractmethod
    def write(self, text: str) -> None: ...


class IOWriter(Writer):
    def write(self, text: str) -> None:
        if text:
            print(text)
