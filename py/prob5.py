#! /usr/bin/env python
# Project Euler problem 5: find smallest positive number that is evenly
# divisible by all numbers from 1-20

from utils import find_prime_factors

def factors_for_nums(nums):
    for n in nums:
        yield (n, find_prime_factors(n, 2))

# Assumes nums are not negative and at least
# one num is positive
def least_common_multiple(nums):
    lcm = 1
    for n, factors in factors_for_nums(nums):
        print(n, factors)
        lcm_tmp = lcm
        for f in factors:
            if lcm_tmp % f != 0:
                lcm *= f
            else:
                lcm_tmp /= f
    return lcm

if __name__ == "__main__":
    nmax = 20
    all_nums = range(1, nmax + 1)
    lcm = least_common_multiple(all_nums)
    print(lcm)
