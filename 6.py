import timeit

def sum_of_squares(n):
    return sum([x**2 for x in xrange(n + 1)])

def square_of_sum(n):
    return sum([x for x in xrange(n + 1)])**2

start_time = timeit.default_timer()

print square_of_sum(100) - sum_of_squares(100)

elapsed = timeit.default_timer() - start_time

print("Evaluated in %.10f seconds." % elapsed)