'''Задача 3.'''
# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

from math import floor, sqrt

def div():
    result = []
    for i in range(3, floor(sqrt(600851475143)), 2):
        if 600851475143 % i == 0:
            for x in range(3, i+1, 2):
                if i % x == 0 and x < i:
                    break
                if x > int(sqrt(i) + 1):
                    result.append(i)
                    break
    print(max(result))

div()