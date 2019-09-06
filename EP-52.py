'''Задача 52'''
# Найдите такое наименьшее положительное целое число x, чтобы 2x, 3x, 4x, 5x и 6x состояли из одних и тех же цифр.

from sys import maxsize


def func(arg):
    for l in arg:
        for i in str(l):
            if i in a:
                continue
            else:
                return None
    return arg


for x in range(2, maxsize ** 10):
    a = str(2 * x)
    b = 3 * x
    c = 4 * x
    d = 5 * x
    e = 6 * x
    lst = [b, c, d, e]
    if func(lst) == lst:
        print(x)
        break
