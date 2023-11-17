# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

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

def fibonacci_partial_sum_fast(from_, to):
    # S(m, n) = S(n) - S(m-1)
    # S(n) = F(n+2) - 1
    # S(m-1) = F(m+1) - 1
    # S(m, n) = F(n+2) - F(m+1)
    if from_ == 0:
        return fast_fib_sum(to)
    else:
        return (fast_fib_sum(to) - fast_fib_sum(from_-1) + 10) % 10
    
if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))
