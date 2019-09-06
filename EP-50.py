'''Задача 50'''
# Простое число 41 можно записать в виде суммы шести последовательных простых чисел:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# Это - самая длинная сумма последовательных простых чисел, в результате которой получается простое число
# меньше одной сотни. Самая длинная сумма последовательных простых чисел, в результате которой получается простое
# число меньше одной тысячи, содержит 21 слагаемое и равна 953. Какое из простых чисел меньше одного миллиона можно
# записать в виде суммы наибольшего количества последовательных простых чисел?

from math import sqrt, floor

max_ = 1000000  # Время работы 4мин


def prime1():
    nums = [1, 2, ]

    for i in range(3, max_, 2):
        for j in range(1, i + 1, 2):
            if j > int(floor(sqrt(i) + 1)):
                nums.append(i)
                break
            elif i % j == 0 and j != 1:
                break
    return nums


def prime2(arg):
    if arg % 2 == 0:
        return None

    for j in range(1, arg + 1, 2):
        if j > int(floor(sqrt(arg) + 1)):
            return arg
        elif arg % j == 0 and j != 1:
            return None


def sum_():
    nums = prime1()
    n = 1
    h = 0
    len_result = 0
    result = 0

    while nums[n] < nums[-1]:
        s = nums[h:n]
        sm = sum(s)
        if prime2(sm) != None:
            if sm < max_ and len_result < len(s):
                result = sm
                len_result = len(s)
            elif sm > max_:
                h += 1
                n = h + 1
        n += 1

    print('result:', result)


sum_()
