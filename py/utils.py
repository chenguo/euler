from itertools import takewhile

def take_limit(seq, limit):
    return takewhile(lambda n: n < limit, seq)

def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def is_even(x):
  return x % 2 == 0

def is_factor(n, f):
  return n % f == 0

def contains_factor(n, factors):
  for f in factors:
    if is_factor(n, f):
      return True
  return False

# Repeatedly divide by increasing divisors. Since
# we're starting with the smallest numbers, every
# new valid factor we find should be a prime
def find_prime_factors(num, start=1):
  factors = []
  largest = 0
  divisor = start
  while divisor < num:
    if num % divisor == 0:
      largest = divisor
      factors.append(divisor)
      num = int(num/divisor)
    else:
      divisor += 1
  if num >= largest:
    factors.append(num)
  return factors
