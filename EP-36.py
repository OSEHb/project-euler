'''Задача 36.'''
# Десятичное число 585 = 10010010012 (в двоичной системе), является палиндромом по обоим основаниям.
# Найдите сумму всех чисел меньше миллиона, являющихся палиндромами по основаниям 10 и 2.
# (Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из оснований).

result = []


def nom2(arg):
    a = bin(arg)
    a = a[2:]

    if a[0] == '0':
        return None

    else:
        pol_m = a[::-1]

        if pol_m == a:
            result.append(i)

        else:
            return None


for i in range(1, 1000000):
    pol_m = str(i)[::-1]

    if i == int(pol_m):
        nom2(i)

print(sum(result))
