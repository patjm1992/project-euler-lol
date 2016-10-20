# Returns list of n fibonacci numbers
def fib(n):
    a = 0
    b = 1
    tmp = 0
    fib_series = []

    while b < n:
        tmp = a
        a = b
        b = tmp + b
        fib_series.append(b)

    return fib_series

even_fibs = filter(lambda x: x % 2 == 0, fib(4000000))

print sum(even_fibs)

