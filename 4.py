def f(n):
    if n == 1:
        return '*'
    elif n == 3:
        return '2'
    elif n % 2 == 0:
        return f(n/2) + '3'
    else:
        return f(n-1) + '1'
print(f(11))
