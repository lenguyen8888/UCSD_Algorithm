# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def fast_gcd(a, b):
    """ Implement a fast iterative GCD algorithm """
    if b == 0:
        return a
    else:
        return fast_gcd(b, a % b)

def fast_lcm(a, b):
    """ Implement a fast iterative LCM algorithm """
    return (a * b) // fast_gcd(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(fast_lcm(a, b))

