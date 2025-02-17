from typing import Any
from app.command import Command, CommandType
from app.database import DataBase
from app.view import CommandView


def execute_command(
    data_base: DataBase,
    command_view: CommandView,
    command: Command,
) -> str:

    return_value: Any = None

    match command.type:
        case CommandType.SET:
            return_value = data_base.set(command.key, command.value)
        case CommandType.GET:
            return_value = data_base.get(command.key)
        case CommandType.UNSET:
            return_value = data_base.unset(command.key)
        case CommandType.COUNTS:
            return_value = data_base.counts(command.value)
        case CommandType.FIND:
            return_value = data_base.find(command.value)

        case CommandType.BEGIN:
            data_base.begin()

        case CommandType.ROLLBACK:
            data_base.rollback()
        case CommandType.COMMIT:
            data_base.commit()

    return command_view.to_string(command.type, return_value)
