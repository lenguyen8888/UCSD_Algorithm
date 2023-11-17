# Uses python3
import sys
DEBUG_FLAG = False


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10

def get_pisano_sequence(m):
    # Pisano sequence always starts with 01
    pisano = [0, 1]
    previous = 0
    current = 1
    while True:
        previous, current = current, (previous + current) % m
        # Pisano sequence always ends with 01
        if previous == 0 and current == 1:
            # remove the last 0, 1 is not part of Pisano sequence yet
            return pisano[:-1]
        pisano.append(current)

def fast_fibonacci_huge(n, m):
    if n <= 1:
        return n
    # find Pisano sequence
    pisano_sequence = get_pisano_sequence(m)
    n = n % len(pisano_sequence)
    return pisano_sequence[n]
    
def fast_fib_sum(n):
    # what is the sum of the first n Fibonacci numbers?
    # S(n) = F(n+2) - 1

    f_n_plus_2 = fast_fibonacci_huge(n+2, 10)
    return (f_n_plus_2 - 1 + 10) % 10
    
# write test_cases to test fast_fib_sum against fibonacci_sum_naive
def test_cases():
    for i in range(20):
        assert fast_fib_sum(i) == fibonacci_sum_naive(i)
    assert fast_fib_sum(3) == 4
    assert fast_fib_sum(100) == 5


if __name__ == '__main__':
    if DEBUG_FLAG:
        test_cases()
    input = sys.stdin.read()
    n = int(input)
    print(fast_fib_sum(n))
