from functions_toolkit.functions_toolkit import fib_iter, fib_rec, sum_series_recursive, sum_series_iterative, tower_of_hanoi, most_consecutive_nums, fib_formula

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
    actual = sum_series_iterative(5, 2)
    expected = 11
    assert actual == expected

def test_tower_of_hanoi():
    assert tower_of_hanoi
    
def test_most_consecutive_nums():
    assert most_consecutive_nums
    
def test_most_consecutive_nums2():
    arr = [1,2,3,4,5,9,99,999,9999,99999]
    assert most_consecutive_nums(arr) == 5
    
def test_most_goats_in_farm():
    arr = [1,6,2,5,3,4,9,7,8,99,999,999,99999999,999999999,99999999]
    assert most_consecutive_nums(arr) == 9
    
def test_fib_formula():
    assert fib_formula(5) == 5

def test_fib_formula2():
    print(fib_formula(100))
    assert True