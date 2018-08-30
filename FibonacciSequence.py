# Returning the nth number of a fibonacci sequence using Recursion
def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

# Returning the nth number of a fibonacci sequence using Memoization
lookup = {}
def fib_dyn(n):
    if n == 0 or n == 1:
        return n
    if not n in lookup:
        lookup[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return lookup[n]

# Returning the nth number of a fibonacci sequence using
def fib_iter(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib_iter(23))
print(fib_dyn(10))
print(fib_rec(10))
