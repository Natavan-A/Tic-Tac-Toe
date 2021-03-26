def increase(variable, amount=1):
    variable += amount

def decrease(variable, amount=1):
    variable -= amount

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        a, b = b, a + b

    return b