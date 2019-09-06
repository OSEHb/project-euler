'''Задача 34.'''
#145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.
#Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.

from math import factorial

result = []

for i in range(3, 100000):
    si = str(i)
    sumfac = 0

    for j in si:
        sumfac += factorial(int(j))

    if sumfac == i:
        result.append(i)

print(sum(result))