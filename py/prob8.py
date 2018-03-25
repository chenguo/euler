#! /usr/bin/env python
# Project Euler problem 8:
# Given a string of numbers, what is the max
# product of some 13 adjcent numbers

def read_nums():
    with open('prob8-input.txt') as f:
        yield from (int(c) for line in f for c in line if c.isdigit())

def mult(xs):
    m = 1
    for x in xs:
        m *= x
    return m

# Compute product of runs of given length in
# given nums sequence
#
# Unnecessarily optimized single pass implementation
def product_runs(nums, length):
    window = []
    product = 1
    for i, n in enumerate(nums):
        if i < length:
            window.append(n)
        else:
            window[i % length] = n
        if len(window) == length:
            yield mult(window)

if __name__ == "__main__":
    nums = read_nums()
    run_length = 13
    result = product_runs(nums, run_length)
    print(max(result))
