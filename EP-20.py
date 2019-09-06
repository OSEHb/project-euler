'''Задача 20'''
# n! означает n × (n − 1) × ... × 3 × 2 × 1
# Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Найдите сумму цифр в числе 100!

from math import factorial
from collections import deque

fac = factorial(100)
nom = deque()
nom += str(fac)
result = 0

while True:
    if len(nom) == 0:
        break
    left = nom.popleft()
    result += int(left)

print(result)
