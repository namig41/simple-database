from pytest import fixture

from app.database import DataBase, MemoryDataBase
from app.parser import Parser, SimpleParser
from app.view import CommandView, SimpleCommandView


@fixture
def parser() -> Parser:
    return SimpleParser()


@fixture
def db() -> DataBase:
    return MemoryDataBase()


@fixture
def view() -> CommandView:
    return SimpleCommandView()
