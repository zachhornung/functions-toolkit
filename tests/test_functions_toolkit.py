from functions_toolkit.functions_toolkit import fib_iter, fib_rec, sum_series_recursive, sum_series_iterative

def test_fib_iter():
    actual = fib_iter(5)
    expected = 5
    assert actual == expected

def test_fib_rec():
    actual = fib_rec(5)
    expected = 5
    assert actual == expected

def test_sum_series_recursive():
    actual = sum_series_recursive(5)
    expected = 5
    assert actual == expected

def test_sum_series_iterative():
    actual = sum_series_iterative(5)
    expected = 5
    assert actual == expected