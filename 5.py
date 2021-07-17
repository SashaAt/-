def f(n): 
    if n < 10:
        return 9
    elif n == 200 or n == 301:
        return 30 + f(n + n%3)
    elif n % 3 == 0:
        return f(n/3) + 11
    else:
        return f(n - n%3) * n

k = 0 # создание переменной, отвечающей за подсчет количества подходящих n
for i in range(100,1201): # перебираем все возможные значения n
    if f(i) > 9 and f(i) < 100 and f(i) % 2 == 0: # проверка условий
        k = k + 1 # увеличиваем количество на 1
print(k)
