# Uses python3
import sys
DEBUG_MODE = False

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def fast_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    # fix previous for loop by adding % 10 before accumulating
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current % 10


def test_fib():
    """ Test function for fast_fib """
    for n in range(20):
        ## assert is used to check if calc_fib and fast_fib return the same value, print passed for n
        assert(fast_fibonacci_last_digit(n) == get_fibonacci_last_digit_naive(n))
        fib_last_dig = fast_fibonacci_last_digit(n)
        print("passed fast_fibonacci_last_digit({}) == get_fibonacci_last_digit_naive({}) == {}".format(n, n, fib_last_dig))
    print()

if __name__ == '__main__':
    if DEBUG_MODE:
        test_fib()
    input = sys.stdin.read()
    n = int(input)
    print(fast_fibonacci_last_digit(n))
