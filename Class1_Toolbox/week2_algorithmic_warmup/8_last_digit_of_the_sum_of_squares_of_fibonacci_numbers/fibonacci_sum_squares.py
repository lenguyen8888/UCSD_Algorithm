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
    pisano = [0, 1]
    previous = 0
    current = 1
    while True:
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return pisano
        pisano.append(current)

def fast_fibonacci_huge(n, m):
    if n <= 1:
        return n
    # find Pisano sequence
    pisano_sequence = get_pisano_sequence(m)
    pisano_period = pisano_sequence[:-1]
    n = n % len(pisano_period)
    return pisano_period[n]

def fast_fib_sum_square(n):
    # what is the sum of the squares of the first n Fibonacci numbers?
    # S(n) = F(n) * F(n+1)
    return (fast_fibonacci_huge(n, 10) * fast_fibonacci_huge(n+1, 10)) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fast_fib_sum_square(n))
