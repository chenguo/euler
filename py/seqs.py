from utils import contains_factor

def inf_range():
  n = 0
  while True:
    yield n
    n += 1

def fibonacci():
  a = 0
  b = 1
  while(True):
    fib = a + b
    yield fib
    a = b
    b = fib

# This implementation is exceedingly slow.
# All primes under 200,000 took ~27s.
# For 2e6, was ungodly long, ~40 minutes
def gen_primes_v1():
  primes = []
  yield 2
  i = 3
  to_print = 10000
  while True:
    if not contains_factor(i, primes):
      if i > to_print:
        to_print += 10000
        print(i)
      yield i
      primes.append(i)
    i += 2

# Sieve method... is actually incredily
# fast. All primes under 200,000 took 0.7s,
# while 2e6 took 2.2s.
# Downside here of course is having to
# pre-allocate the max size of your sieve
def gen_primes_v2():
  limit = 3000000
  nums = [True] * limit
  nums[0] = False
  i = 2
  while i < limit:
    while nums[i-1] == False:
      i += 1
    yield i

    multiple = 2 * i
    while multiple - 1 < limit:
      nums[multiple - 1] = False
      multiple += i
    i += 1

# Dynamic sieve method. Significantly faster,
# 0.17s for 2e5, 1.1s for 2e6.
# Best guess, less memory usage, more
# cache locality, less page faults
def gen_primes_v3():
  limit = 16
  sieve = [True] * limit
  sieve[0] = False
  n_processed = 1
  while True:
    for i in range(n_processed, limit):
      if sieve[i]:
        prime_num = i + 1
        yield prime_num
        multiple_idx = i + prime_num
        _mark_sieve_nonprime(sieve, multiple_idx, prime_num, limit)
    (sieve, new_limit) = _realloc_sieve(sieve, limit)
    n_processed = limit
    limit = new_limit

def _mark_sieve_nonprime(sieve, start_idx, increment, limit):
  idx = start_idx
  while idx < limit:
    sieve[idx] = False
    idx += increment

def _realloc_sieve(sieve, limit):
  sieve.extend([True] * limit)
  new_limit = limit * 2
  for i in range(1, limit):
    if sieve[i]:
      prime_num = i + 1
      multiple = limit - (limit % prime_num)
      multiple_idx = multiple + prime_num - 1
      # In the newly allocated region, sieve multiples of primes
      # found thus far
      _mark_sieve_nonprime(sieve, multiple_idx, prime_num, new_limit)
  return (sieve, new_limit)

# Odd numbers only version of dynamic sieve. The
# indexing gets a bit crazy.
# Cuts run time roughly in half, about expected
# I guess.
# 2e5 limit: 0.11s
# 2e6 limit: 0.62s
def gen_primes():
  limit = 2
  sieve = [True] * limit
  # skipping all even numbers, we assume number = idx * 2 + 1
  yield 2
  n_processed = 1
  while True:
    for i in range(n_processed, limit):
      if sieve[i]:
        prime_num = i*2 + 1
        yield prime_num
        multiple_idx = i + prime_num
        _mark_sieve_nonprime(sieve, multiple_idx, prime_num, limit)
    (sieve, new_limit) = _realloc_sieve_odd(sieve, limit)
    n_processed = limit
    limit = new_limit

def _next_multiple_within_limit_odd(idx, prime_num, limit):
  # Find the last multiple of prime_num just before limit,
  # while accounting for the num = 2*idx + 1 math.
  #
  # In words (which may be more confusing than the math),
  # remove the idx offset from limit, mod by the
  # prime number (which now represents a step of 2x prime_num,
  # since every other multiple of an odd number is even
  # and thus never even considered), and then re-add
  # the idx offset
  #
  # There are corner cases where we end up at the original
  # idx offset, which represents a prime number. In this
  # case we bump to the next represented multiple
  # by adding the step size of prime_num
  tmp_lim = limit - idx
  multiple = tmp_lim - (tmp_lim % prime_num) + idx
  if multiple == idx:
    multiple += prime_num
  return multiple

def _realloc_sieve_odd(sieve, limit):
  sieve.extend([True] * limit)
  new_limit = 2 * limit
  for i in range(1, limit):
    if sieve[i]:
      prime_num = i*2 + 1
      next_multiple = _next_multiple_within_limit_odd(i, prime_num, limit)
      # In the newly allocated region, sieve multiples of primes
      # found thus far. Note while num = i*2 + 1, the step size is still
      # prime_num. This is because every other multiple of an odd number
      # is even and thus not represented
      _mark_sieve_nonprime(sieve, next_multiple, prime_num, new_limit)
  return (sieve, new_limit)
