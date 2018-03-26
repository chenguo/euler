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

def gen_primes():
    primes = []
    i = 2
    while True:
        if not contains_factor(i, primes):
            yield i
            primes.append(i)
        i += 1
