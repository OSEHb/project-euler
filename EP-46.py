'''Задача 46'''
# Кристиан Гольдбах показал, что любое нечетное составное число можно записать в виде суммы простого числа и
# удвоенного квадрата.
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
# Оказалось, что данная гипотеза неверна.
# Каково наименьшее нечетное составное число, которое нельзя записать в виде суммы простого числа и удвоенного квадрата?

from sys import maxsize
from math import sqrt, floor

noms = []  # Время работы 3мин 40с
numbers = []
result = False


def nom():  # Находим число для удвоенного квадрата
    for k in range(1, floor(((i - n) / 2) + 1)):
        numbers.append(k)


def func(arg):  # Находим простое число
    for x in range(3, arg, 2):
        for y in range(1, x + 1, 2):
            if y > int(floor(sqrt(x) + 1)):
                noms.append(x)
                break

            elif x % y == 0 and y != 1:
                break


for i in range(35, maxsize ** 10, 2):
    if result == True:
        break
    print(i)
    index = 0

    for j in range(3, i, 2):
        if index > 0 or result == True:
            break

        if i % j == 0:
            noms = []
            func(i)
            for n in noms:
                if index > 0:
                    break

                numbers = []
                nom()
                for num in numbers:
                    if i == n + (2 * (num ** 2)):
                        index += 1
                        break

            if index == 0:
                result = True
                print('result:', i)
                break

