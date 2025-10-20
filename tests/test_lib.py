from src.fib import fib


def test_fib_base_cases():
    assert fib(0) == 1
    assert fib(1) == 1


def test_fib_sequence():
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(4) == 5
    assert fib(5) == 8
    assert fib(10) == 89
