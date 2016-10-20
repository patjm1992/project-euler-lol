import timeit

def is_palidrome(n):
    n = str(n)

    if n == n[::-1]:
        return True
    else:
        return False

start_time = timeit.default_timer()

res = 0

for a in range(999, 0, -1):
    for b in range(a, 0, -1):
        prod = a * b
        if is_palidrome(prod):
            if prod > res:
                res = prod

elapsed = timeit.default_timer() - start_time

print res

print("Evaluated in %.10f seconds." % elapsed)