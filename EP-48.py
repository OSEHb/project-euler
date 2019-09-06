'''Задача 48'''
# Сумма 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
# Найдите последние десять цифр суммы 1**1 + 2**2 + 3**3 + ... + 1000**1000.

result = ''
index = 0


def func(a, b):
    num = 0
    for i in range(a, b + 1):
        num += i ** i

    num = str(num)
    return num


for n in reversed(func(1, 1000)):
    if index == 10:
        print(result[::-1])
        break

    else:
        result += n
        index += 1
