from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Iterable


class DataBase(ABC):
    @abstractmethod
    def set(self, key: str, value: int) -> None: ...

    @abstractmethod
    def get(self, key: str) -> int | None: ...

    @abstractmethod
    def unset(self, key: str) -> None: ...

    @abstractmethod
    def counts(self, value: int) -> int: ...

    @abstractmethod
    def find(self, value: int) -> Iterable[str]: ...

    @abstractmethod
    def begin(self) -> None: ...

    @abstractmethod
    def rollback(self) -> None: ...

    @abstractmethod
    def commit(self) -> None: ...


@dataclass
class MemoryDataBase(DataBase):

    memory: dict[str, int] = field(default_factory=dict)
    transactions: list = field(default_factory=list)

    def set(self, key: str, value: int) -> None:
        self.memory[key] = value

    def get(self, key: str) -> int | None:
        return self.memory.get(key, None)

    def unset(self, key: str) -> None:
        if key in self.memory:
            del self.memory[key]

    def counts(self, value: int) -> int:
        result: int = 0

        for v in self.memory.values():
            if v == value:
                result += 1

        return result

    def find(self, value: int) -> Iterable[str]:
        keys: list[str] = []

        for key, v in self.memory.items():
            if v == value:
                keys.append(key)

        return keys

    def begin(self) -> None:
        self.transactions.append(self.memory.copy())

    def rollback(self) -> None:
        if self.transactions:
            self.memory = self.transactions.pop()

    def commit(self) -> None:
        if self.transactions:
            self.transactions = []
