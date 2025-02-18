from abc import abstractmethod
from dataclasses import dataclass
from typing import Any, Protocol
from app.command import CommandType


class CommandView(Protocol):
    @abstractmethod
    def to_string(self, type: CommandType, value: Any) -> str: ...


@dataclass
class SimpleCommandView(CommandView):
    def to_string(self, type: CommandType, value: Any) -> str:
        match type:
            case CommandType.GET:
                if value is None:
                    return "NULL"
                return str(value)
            case CommandType.COUNTS:
                return str(value)
            case CommandType.FIND:
                return ", ".join(value)

        return ""
