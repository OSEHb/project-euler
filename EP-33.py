'''Задача 33.'''
#  Дробь 49/98 является любопытной, поскольку неопытный математик, пытаясь сократить ее, будет ошибочно полагать,
#  что 49/98 = 4/8, являющееся истиной, получено вычеркиванием девяток.
#  Дроби вида 30/50 = 3/5 будем считать тривиальными примерами.
#  Существует ровно 4 нетривиальных примера дробей подобного типа, которые меньше единицы и содержат двухзначные числа
#  как в числителе, так и в знаменателе.
#  Пусть произведение этих четырех дробей дано в виде несократимой дроби (числитель и знаменатель дроби не имеют
#  общих сомножителей). Найдите знаменатель этой дроби.

from fractions import Fraction  # Сокращает дробь

nums = 1
dens = 1

for num in range(10, 100):
    for den in range(num + 1, 100):
        num_str = str(num)
        den_str = str(den)

        if num_str[0] == '0' or num_str[1] == '0' or den_str[0] == '0' or den_str[1] == '0':
            continue

        else:
            if num_str[1] == den_str[0] and int(num_str[0]) / int(den_str[1]) == num / den:
                print(num_str[0], '/', den_str[1])
                nums *= int(num_str[0])
                dens *= int(den_str[1])

print('result:', Fraction(nums, dens))
