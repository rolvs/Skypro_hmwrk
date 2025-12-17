import pytest

from src.decorators import log


def test_log_success_console(capsys):
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)

    captured = capsys.readouterr()
    assert result == 3
    assert captured.out.strip() == "my_function ok"


def test_log_error_console(capsys):
    @log()
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    captured = capsys.readouterr()
    out = captured.out.strip()

    assert "my_function error: ZeroDivisionError." in out
    assert "Inputs: (1, 0), {}" in out


def test_log_success_to_file(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)

    assert result == 3
    assert log_file.read_text(encoding="utf-8").strip() == "my_function ok"


def test_log_error_to_file(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        my_function(1, 0)

    text = log_file.read_text(encoding="utf-8").strip()
    assert "my_function error: ZeroDivisionError." in text
    assert "Inputs: (1, 0), {}" in text
