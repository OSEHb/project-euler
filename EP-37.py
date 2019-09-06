'''Задача 37.'''
# Число 3797 обладает интересным свойством. Будучи само по себе простым числом, из него можно последовательно
# выбрасывать цифры слева направо, число же при этом остается простым на каждом этапе: 3797, 797, 97, 7.
# Точно таким же способом можно выбрасывать цифры справа налево: 3797, 379, 37, 3.
# Найдите сумму единственных одиннадцати простых чисел, из которых можно выбрасывать цифры как справа налево,
# так и слева направо, но числа при этом остаются простыми.
# ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются.

from sys import maxsize
from math import sqrt

result = []  # Время работы 24 сек


def func(arg):
    x = arg
    y = arg

    while True:
        a = str(x)[1:]
        x = int(a)

        for n in range(1, x + 1, 2):
            if x == 0 or x == 1:
                return None

            elif x % 2 == 0 and x != 2:
                return None

            if n > int((sqrt(x)) + 1):
                break

            elif x % n == 0 and n != 1:
                return None

        if len(str(x)) == 1:
            while True:
                b = str(y)[0:-1]
                y = int(b)

                for n in range(1, y + 1, 2):
                    if y == 0 or y == 1:
                        return None

                    elif y % 2 == 0 and y != 2:
                        return None

                    if n > int((sqrt(y)) + 1):
                        break

                    elif y % n == 0 and n != 1:
                        return None

                if len(str(y)) == 1:
                    return result.append(i)


for i in range(11, maxsize ** 10, 2):
    if len(result) == 11:
        break

    for j in range(3, i + 1, 2):
        if j > int((sqrt(i)) + 1):
            func(i)
            break

        elif i % j == 0:
            break

print('result:', sum(result))

