def f(n):
    if n > 6:
        return f(n-2)+ g(n-3)
    else:
        return 3
def g(n):
    if n > 6:
        return g(n-2) + f(n-2)
    else:
        return 3

print(f(14))
