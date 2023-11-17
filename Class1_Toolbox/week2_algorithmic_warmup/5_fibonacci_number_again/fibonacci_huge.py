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

