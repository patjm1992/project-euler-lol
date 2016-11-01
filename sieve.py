import timeit
import math

# Sieve of Eratosthenes algorithm
def sieve(n):

    # List containing 2 and odd numbers
    nums = [x for x in xrange(2, n) if x == 2 or x % 2 != 0]

    p = 2

    for p in nums:
        for i in xrange(p + p, n + 1, p):
            if i in nums:
                nums.remove(i)
    return nums

start_time = timeit.default_timer()

print sieve(100000)

elapsed = timeit.default_timer() - start_time

print("Evaluated in %.10f seconds." % elapsed)