from functions_toolkit.functions_toolkit import fibonacci_iterative, fibonacci_recursive

def test_fibonacci_iterative():
    actual = fibonacci_iterative(5)
    expected = 5
    assert actual == expected
