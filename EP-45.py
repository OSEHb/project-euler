'''Задача 45'''
# Треугольные, пятиугольные и шестиугольные числа вычисляются по нижеследующим формулам:
# Треугольные	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Пятиугольные	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Шестиугольные	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# Можно убедиться в том, что T285 = P165 = H143 = 40755.#
# Найдите следующее треугольное число, являющееся также пятиугольным и шестиугольным.

from math import sqrt, ceil
from sys import maxsize

t = 286

for n in range(t, maxsize ** 10):
    tn = int((n * (n + 1)) / 2)
    np = ceil(sqrt((tn * 2) / 3))

    if tn == (np * ((3 * np) - 1)) / 2:
        nh = ceil(sqrt(tn / 2))

        if tn == nh * ((2 * nh) - 1):
            print('result:', tn)
            break

    else:
        continue