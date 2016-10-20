import timeit

start_time = timeit.default_timer()

print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))

elapsed = timeit.default_timer() - start_time

print("Evaluated in %.10f seconds." % elapsed)
