# Uses python3
import sys
DEBUG_FLAG = False

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

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
# write test_cases 2816213588 239
def test_cases():
    assert fast_fibonacci_huge(2816213588, 239) == 151
    assert fast_fibonacci_huge(239, 1000) == 161
    assert fast_fibonacci_huge(2816213588, 30524) == 10249
 
if __name__ == '__main__':
    if DEBUG_FLAG:
        test_cases()

    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fast_fibonacci_huge(n, m))

