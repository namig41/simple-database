from dataclasses import dataclass
from enum import StrEnum


class CommandType(StrEnum):
    SET = "SET"
    GET = "GET"
    UNSET = "UNSET"
    COUNTS = "COUNTS"
    FIND = "FIND"
    END = "END"

    BEGIN = "BEGIN"
    ROLLBACK = "ROLLBACK"
    COMMIT = "COMMIT"


@dataclass
class Command:
    type: CommandType
    key: str | None = None
    value: int | None = None

    def __post_init__(self):
        self._validate()

    def _validate(self) -> None:
        if self.type == CommandType.SET:
            if self.key is None or self.value is None:
                raise ValueError("The key must be specified for SET command.")

        if self.type == CommandType.GET:
            if self.key is None:
                raise ValueError("The key must be specified for GET command.")

        if self.type == {CommandType.COUNTS, CommandType.FIND}:
            if self.value is None:
                raise ValueError(
                    "The value must be specified for {self.type.value} command."
                )

    @classmethod
    def build(
        cls,
        command_type: CommandType,
        key: str | None,
        value: int | None,
    ) -> "Command":
        return cls(command_type, key, value)
