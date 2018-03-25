#! /usr/bin/env python
# Project Euler problem 9:
# Find a pythogorean triplet such that the following are true:
# a < b < c
# a^2 + b^2 = c^2
# a + b + c = 1000


# Increment two dividing lines i and j splitting
# total into three chunks:
# a | b | c
# hence:
# a = i
# b = j - i
# c = total - j
def gen_ordered_triplets(total):
    i = 0
    j = 1
    while total - j > j - i:
        while j - i > i:
            yield (i, j - i, total - j)
            i += 1
        j += 1
        i = max(0, j - (total - j) + 1)

def is_pythag_triplet(a, b, c):
    return a < b and b < c and a*a + b*b == c*c

def find_pythagorean_triplet(total):
    for a, b, c in gen_ordered_triplets(total):
        if is_pythag_triplet(a, b, c):
            return (a, b, c)
    return None

if __name__ == "__main__":
  total = 1000
  triplet = find_pythagorean_triplet(total)
  if triplet != None:
      print("triplet " + str(triplet))
      (a, b, c) = triplet
      print("product " + str(a*b*c))
  else:
      print("Failed to find Pythagorean triplet summing to " + str(total))
