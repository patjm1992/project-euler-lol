import timeit
import math

start_time = timeit.de fault_timer()

target = 600851475143
n = 2

while target > 1:
    if target % n == 0:
        target = target / n
    else:
        n += 1

print n

elapsed = timeit.default_timer() - start_time

print("Evaluated in %.10f seconds." % elapsed)