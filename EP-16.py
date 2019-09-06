'''Задача 16.'''
# 2**15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
# Какова сумма цифр числа 2**1000?

from collections import deque

a = 2 ** 1000
a = str(a)


def ep_15():
    turn = deque()
    turn += a
    result = 0

    while a:
        nom = turn.popleft()
        result += int(nom)
        if len(turn) == 0:
            break

    print(result)


ep_15()
