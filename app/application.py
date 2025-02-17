from dataclasses import dataclass
import logging

from app.command import Command, CommandType
from app.database import DataBase, MemoryDataBase
from app.execute import execute_command
from app.parser import Parser, SimpleParser
from app.reader import IOReader, Reader
from app.view import CommandView, SimpleCommandView
from app.writer import IOWriter, Writer

logger = logging.getLogger(__name__)


@dataclass
class Application:
    database: DataBase
    parser: Parser
    reader: Reader
    writer: Writer
    view: CommandView

    run_flag: bool = True

    def run(self) -> None:

        while self.run_flag:
            try:
                line: str = self.reader.read()
                command: Command = self.parser.parse(line)

                if command.type == CommandType.END:
                    break

                text: str = execute_command(
                    data_base=self.database,
                    command_view=self.view,
                    command=command,
                )
                self.writer.write(text)
            except (EOFError, KeyboardInterrupt):
                self.run_flag = False
            except Exception as exception:
                logger.error(exception)


def create_app() -> Application:
    return Application(
        database=MemoryDataBase(),
        parser=SimpleParser(),
        reader=IOReader(),
        writer=IOWriter(),
        view=SimpleCommandView(),
    )
