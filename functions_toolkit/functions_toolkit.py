# Iterative way to do Fibonacci sequence. returns Fibonacci number at the given index
def fib_iter(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
    return a


# Recursive way to do Fibonacci sequence. Returns Fibonacci number at the given index.
def fib_rec(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib_rec(num-1) + fib_rec(num-2)


# General way to generate a sequence of numbers recursively. takes 1 positional argument, and 2 keyword arguments
def sum_series_recursive(num, a=0, b=1):
    if num == a:
        return a
    if num == b:
        return b
    return sum_series_recursive(num-1, a, b) + sum_series_recursive(num-2, a, b)


def sum_series_iterative(num, starting1=0, starting2=1):
    a,b = starting1,starting2
    for _ in range(num):
        a,b = b, a+b
    return a

def tower_of_hanoi(num, from_rod, to_rod, aux_rod):
    if num == 1:
        print(f'\nMove disk 1 from rod {from_rod} to rod {to_rod}')
        return
    tower_of_hanoi(num-1, from_rod, aux_rod, to_rod)
    print(f'\nMove disk {num} from rod {from_rod} to rod {to_rod}')
    tower_of_hanoi(num-1, aux_rod, to_rod, from_rod)

if __name__ == '__main__':
    tower_of_hanoi(3, 'a', 'b', 'c',)