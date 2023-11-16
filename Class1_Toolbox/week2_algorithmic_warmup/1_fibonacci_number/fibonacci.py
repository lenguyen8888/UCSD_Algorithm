# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fast_fib(n):
    """ My fast_fib solution that use iteration
    from the bottom up """
    if n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

def fast_fib2(n):
    """ My fast_fib solution that use iteration
    from the top down """
    if n <= 1:
        return n
    else:
        ## use 2 variables to store the previous 2 values
        prev1 = 1
        prev2 = 0
        for i in range(2, n + 1):
            fib = prev1 + prev2
            prev2 = prev1
            prev1 = fib
        return fib

def test_fib():
    """ Test function for fast_fib """
    for n in range(20):
        ## assert is used to check if calc_fib and fast_fib return the same value, print passed for n
        assert(fast_fib(n) == calc_fib(n))
        print("passed fast_fib({}) == calc_fib({})".format(n, n))
        ## check if fast_fib2 returns the same value as fast_fib for n
        assert(fast_fib2(n) == fast_fib(n))        
        print("passed fast_fib2({}) == fast_fib({})".format(n, n))
    print()

if __name__ == '__main__':
    # test_fib()
    n = int(input())
    print(fast_fib2(n))


