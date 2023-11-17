# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def get_pisano_sequence(m):
    # Pisano sequence always starts with 01
    # where can we read about Pisano sequence?
    # https://en.wikipedia.org/wiki/Pisano_period

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
    # since Pisano sequence is periodic, the length of
    # the sequence is the same as the length of the remainder
    n = n % len(pisano_sequence)
    # we can find the nth element of the Pisano sequence as the remainder
    # of the nth element of the Fibonacci sequence divided by m
    return pisano_sequence[n]

def fast_fib_sum_square(n):
    # what is the sum of the squares of the first n Fibonacci numbers?
    # S(n) = F(n) * F(n+1)
    return (fast_fibonacci_huge(n, 10) * fast_fibonacci_huge(n+1, 10)) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fast_fib_sum_square(n))
