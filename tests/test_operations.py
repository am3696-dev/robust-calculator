import pytest
from calculator.app import add, subtract, multiply, divide, main
from unittest.mock import patch

# ----------------------
# Function tests
# ----------------------
@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_add_param(a, b, expected):
    """Parameterized test for the add function."""
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [(5, 2, 3), (2, 5, -3), (0, 0, 0)])
def test_subtract_param(a, b, expected):
    """Parameterized test for the subtract function."""
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [(3, 4, 12), (-2, 3, -6), (0, 10, 0)])
def test_multiply_param(a, b, expected):
    """Parameterized test for the multiply function."""
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [(10, 2, 5), (5, 2, 2.5)])
def test_divide_param(a, b, expected):
    """Parameterized test for the divide function."""
    assert divide(a, b) == expected

@pytest.mark.parametrize("a,b", [(5, 0), (10, 0)])
def test_divide_zero(a, b):
    """Test divide by zero error handling."""
    with pytest.raises(ValueError):
        divide(a, b)

# ----------------------
# CLI tests (simulate user input)
# ----------------------
def test_main_quit(capsys):
    """Tests the 'quit' command."""
    with patch("builtins.input", side_effect=["quit"]):
        main()
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out

def test_main_add(capsys):
    """Tests the addition operation."""
    with patch("builtins.input", side_effect=["add", "2", "3", "quit"]):
        main()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out

def test_main_subtract(capsys):
    """Tests the subtraction operation."""
    with patch("builtins.input", side_effect=["subtract", "5", "3", "quit"]):
        main()
    captured = capsys.readouterr()
    assert "Result: 2.0" in captured.out

def test_main_multiply(capsys):
    """Tests the multiplication operation."""
    with patch("builtins.input", side_effect=["multiply", "2", "3", "quit"]):
        main()
    captured = capsys.readouterr()
    assert "Result: 6.0" in captured.out

def test_main_divide(capsys):
    """Tests the division operation."""
    with patch("builtins.input", side_effect=["divide", "6", "2", "quit"]):
        main()
    captured = capsys.readouterr()
    assert "Result: 3.0" in captured.out

def test_main_invalid_operation(capsys):
    """Tests an invalid operation."""
    with patch("builtins.input", side_effect=["invalid", "quit"]):
        main()
    captured = capsys.readouterr()
    assert "Invalid operation" in captured.out

def test_main_invalid_number_first(capsys):
    """Tests a non-numeric input for the first number."""
    with patch("builtins.input", side_effect=["add", "two", "3", "quit"]):
        main()
    captured = capsys.readouterr()
    assert "Error: could not convert string to float: 'two'" in captured.out

def test_main_invalid_number_second(capsys):
    """Tests a non-numeric input for the second number."""
    with patch("builtins.input", side_effect=["add", "2", "three", "quit"]):
        main()
    captured = capsys.readouterr()
    assert "Error: could not convert string to float: 'three'" in captured.out

def test_main_divide_by_zero(capsys):
    """Tests division by zero handling."""
    with patch("builtins.input", side_effect=["divide", "5", "0", "quit"]):
        main()
    captured = capsys.readouterr()
    assert "Error: Cannot divide by zero" in captured.out

def test_main_operation_case_insensitive(capsys):
    """Tests that the operation is case-insensitive."""
    with patch("builtins.input", side_effect=["ADD", "2", "3", "quit"]):
        main()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out

def test_main_empty_input(capsys):
    """Tests an empty input for the operation."""
    with patch("builtins.input", side_effect=["", "quit"]):
        main()
    captured = capsys.readouterr()
    assert "Invalid operation" in captured.out

def test_main_whitespace_input(capsys):
    """Tests an operation with leading/trailing whitespace."""
    with patch("builtins.input", side_effect=["  add  ", "2", "3", "quit"]):
        main()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out

def test_main_generic_exception(capsys):
    """Tests that any unexpected error is caught by the generic handler."""
    def faulty_add(a, b):
        raise RuntimeError("Test exception")
    
    with patch("calculator.app.add", side_effect=faulty_add):
        with patch("builtins.input", side_effect=["add", "2", "3", "quit"]):
            main()
    captured = capsys.readouterr()
    assert "An unexpected error occurred: Test exception" in captured.out
