#! /usr/bin/env python
# Project Euler problem 6:
# For xs, find sum(x)^2 - sum(x^2), where xs are the first
# 100 natural numbers

def sum_sq(nums):
    return sum(n*n for n in nums)

if __name__ == "__main__":
    nmax = 100
    nums = range(1, nmax + 1)
    result = sum(nums)**2 - sum_sq(nums)
    print(result)
