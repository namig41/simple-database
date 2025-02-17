import pytest
from app.command import CommandType


def test_parse_set_command_with_key_and_value(parser):
    line = "SET A 10"
    command = parser.parse(line)

    assert command.type == CommandType.SET
    assert command.key == "A"
    assert command.value == 10


def test_parse_get_command_with_key(parser):
    line = "GET A"
    command = parser.parse(line)

    assert command.type == CommandType.GET
    assert command.key == "A"
    assert command.value is None


def test_parse_counts_command_with_value(parser):
    line = "COUNTS 10"
    command = parser.parse(line)

    assert command.type == CommandType.COUNTS
    assert command.key is None
    assert command.value == 10


def test_parse_find_command_with_value(parser):
    line = "FIND 10"
    command = parser.parse(line)

    assert command.type == CommandType.FIND
    assert command.key is None
    assert command.value == 10


def test_parse_unexpected_arguments(parser):
    line = "SET A 10 extra"
    with pytest.raises(Exception, match="Unexpected arguments size"):
        parser.parse(line)


def test_parse_set_command_missing_key(parser):
    line = "SET A A A"
    with pytest.raises(Exception, match="Unexpected arguments size"):
        parser.parse(line)


def test_parse_set_command_missing_value(parser):
    line = "SET A 10 10"
    with pytest.raises(Exception, match="Unexpected arguments size"):
        parser.parse(line)
