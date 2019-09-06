'''Задача 12.'''
# Последовательность треугольных чисел образуется путем сложения натуральных чисел.
# К примеру, 7-ое треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# Первые десять треугольных чисел:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Перечислим делители первых семи треугольных чисел:
#  1: 1
#  3: 1, 3
#  6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28
# Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.
# Каково первое треугольное число, у которого более пятисот делителей?

import sys
from math import ceil, sqrt

result = []
num = 0
for i in range(1, sys.maxsize ** 10):  # Время работы: 80сек
    num += i
    for x in range(1, num + 1):
        if num % x == 0 and x < ceil(sqrt(num)):  # Корени для ускорения
            result.append(x)
            qx = num // x  # Ответный делитель меньшему
            result.append(qx)
        elif x >= ceil(sqrt(num)):
            break
    if len(result) > 500:
        break
    else:
        result = []

print(num)