def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def my_max_pairwise_product(numbers):
    """ My solution for the problem """
    # Find the first max number
    max1 = max(numbers)
    # Remove it from the list
    numbers.remove(max1)
    # Find the second max number
    max2 = max(numbers)
    # Return the product
    return max1 * max2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(my_max_pairwise_product(input_numbers))
