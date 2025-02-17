from app.command import CommandType


def test_to_string_get_command_with_value(view):
    result = view.to_string(CommandType.GET, 10)
    assert result == "10"


def test_to_string_get_command_with_none(view):
    result = view.to_string(CommandType.GET, None)
    assert result == "NULL"


def test_to_string_counts_command(view):
    result = view.to_string(CommandType.COUNTS, 5)
    assert result == "5"


def test_to_string_find_command_with_multiple_values(view):
    result = view.to_string(CommandType.FIND, ["A", "B", "C"])
    assert result == "A, B, C"


def test_to_string_find_command_with_single_value(view):
    result = view.to_string(CommandType.FIND, ["A"])
    assert result == "A"


def test_to_string_empty_find_command(view):
    result = view.to_string(CommandType.FIND, [])
    assert result == ""


def test_to_string_empty_case(view):
    result = view.to_string(CommandType.END, None)
    assert result == ""
