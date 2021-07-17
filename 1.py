def f(n):
    if n == 1:
        return n + 4
    elif n % 2 == 0:
        return f(n/2) + 2
    else:
        return f(n-1) + 1

print(f(10))
