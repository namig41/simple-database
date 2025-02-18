from abc import abstractmethod
from typing import Protocol

from app.command import Command, CommandType


class Parser(Protocol):
    @abstractmethod
    def parse(self, line: str) -> Command: ...


class SimpleParser(Parser):
    def parse(self, line: str) -> Command:
        args: list[str] = line.split()

        command_type: str = args[0]
        key: str | None = None
        value: int | None = None

        match len(args):
            case 1:
                ...
            case 2:
                if command_type in {"FIND", "COUNTS"}:
                    value = int(args[1])
                else:
                    key = args[1]
            case 3:
                key, value_str = args[1], args[2]
                value = int(value_str)
            case _:
                raise Exception("Unexpected arguments size")

        return Command(
            type=CommandType(command_type),
            key=key,
            value=value,
        )
