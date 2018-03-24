#! /usr/bin/env python
# Project Euler problem 4: Find the largest product of two 3-digit numbers
# that is also a palindrome

from heapq import heappush, heappop
from utils import is_palindrome

def num_is_palindrome(n):
    return is_palindrome(str(n))

# Python does not have a max heap, so we
# have to use negative numbers with the
# default min heap
def q_entry(n1, n2):
    return (-n1 * n2, n1, n2)

def largest_palindrome_product(n1, n2):
    q = []
    heappush(q, q_entry(n1, n2))
    while len(q) > 0:
        (index, v1, v2) = heappop(q)
        prod = -1 * index
        if num_is_palindrome(prod):
            return prod
        else:
            heappush(q, q_entry(v1, v2 - 1))
            if v1 == v2:
                heappush(q, q_entry(v1 - 1, v2 - 1))

if __name__ == "__main__":
    n_max = 999
    result = largest_palindrome_product(n_max, n_max)
    print(result)
