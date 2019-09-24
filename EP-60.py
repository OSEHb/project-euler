'''Задача 60'''
# Простые числа 3, 7, 109 и 673 достаточно замечательны. Если взять любые два из них и объединить их в произвольном
# # порядке, в результате всегда получится простое число. Например, взяв 7 и 109, получатся простые числа 7109 и 1097.
# # Сумма этих четырех простых чисел, 792, представляет собой наименьшую сумму элементов множества из четырех простых чисел,
# # обладающих данным свойством.
# # Найдите наименьшую сумму элементов множества из 5 простых чисел,
# # для которых объединение любых двух даст новое простое число.

from itertools import permutations
from math import floor, sqrt

prime_nums = []  # Время работы 8мин


def func2(arg):  # Объединяем и проверяем простое ли это число
    result = True
    print(arg)

    for prime_unit in permutations(arg, 2):
        prime_unit = int(str(prime_unit[0]) + str(prime_unit[1]))
        if result == False:
            break

        for n in range(1, prime_unit + 1, 2):
            if n > int(floor(sqrt(prime_unit) + 1)):
                break
            elif prime_unit % n == 0 and n != 1:
                result = False
                break

    if result == True:
        return sum(arg)

    return None


def func(arg):  # Берём пять простых чисел, по ходу проверяя их на условие
    for n1 in arg:
        for n2 in arg[arg.index(n1) + 1:arg[-1]]:
            if func2([n1, n2]) == None:
                continue
            for n3 in arg[arg.index(n2) + 1:arg[-1]]:
                if func2([n1, n2, n3]) == None:
                    continue
                for n4 in arg[arg.index(n3) + 1:arg[-1]]:
                    if func2([n1, n2, n3, n4]) == None:
                        continue
                    for n5 in arg[arg.index(n4) + 1:arg[-1]]:
                        nums_5 = [n1, n2, n3, n4, n5]
                        result = func2(nums_5)

                        if result != None:
                            return [nums_5, result]

    return None


for prime in range(3, 10000, 2):  # Все простые числа до 10000
    for num in range(1, prime + 1, 2):
        if num > int(floor(sqrt(prime) + 1)):
            prime_nums.append(prime)
            break
        elif prime % num == 0 and num != 1:
            break

f = func(prime_nums)
if f != None:
    print()
    print(f[0])
    print('result:', f[1])
else:
    print(f)
