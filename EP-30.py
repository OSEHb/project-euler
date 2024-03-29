'''Задача 30.'''
# Удивительно, но существует только три числа, которые могут быть записаны в виде суммы четвертых степеней их цифр:
# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4
# 1 = 14 не считается, так как это - не сумма.
# Сумма этих чисел равна 1634 + 8208 + 9474 = 19316.
# Найдите сумму всех чисел, которые могут быть записаны в виде суммы пятых степеней их цифр.

table = {}
result = []

for j in range(0, 10):
    table[j] = j ** 5

for noms in range(10, 1000000):
    n = list(str(noms))
    sum_ = 0

    for nom in n:
        sum_ += table[int(nom)]

    if sum_ == noms:
        result.append(sum_)

print(sum(result))
