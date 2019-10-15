'''Задача 61'''
# К фигурным (многоугольным) числам относятся треугольные, квадратные, пятиугольные, шестиугольные,
# семиугольные и восьмиугольные числа, которые расчитываются по следующим формулам:
#
# Треугольные	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Квадратные	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
# Пятиугольные	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Шестиугольные	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
# Семиугольные	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
# Восьмиугольные	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
# Упорядоченное множество из трех четырехзначных чисел: 8128, 2882, 8281, обладает тремя интересными свойствами
#
# Множество является цикличным: последние две цифры каждого числа являются первыми двумя цифрами
# следующего (включая последнее и первое числа).
# Каждый тип многоугольника — треугольник (P3,127=8128), квадрат (P4,91=8281) и пятиугольник (P5,44=2882) — представлены
# различными числами данного множества.
# Это — единственное множество четырехзначных чисел, обладающее указанными свойствами.
# Найдите сумму элементов единственного упорядоченного множества из шести цикличных четырехзначных чисел,
# в котором каждый тип многоугольников — треугольник, квадрат, пятиугольник, шестиугольник, семиугольник и
# восьмиугольник — представлены различными числами этого множества.

from sys import maxsize

table = {
    'triangle_nums': [],
    'square_nums': [],
    'pentagonal_nums': [],
    'hexagonal_nums': [],
    'heptagonal_nums': [],
    'octagonal_nums': [],
}

# находим все фигурные числа каждого многоугольного числа с 4 цифрами в числе и заносим в словарь.
for n in range(1, maxsize ** 10):
    i = n * (n + 1) // 2

    if len(str(i)) >= 5:
        break
    elif len(str(i)) == 4:
        table['triangle_nums'].append(i)

for n in range(1, maxsize ** 10):
    i = n ** 2

    if len(str(i)) >= 5:
        break
    elif len(str(i)) == 4:
        table['square_nums'].append(i)

for n in range(1, maxsize ** 10):
    i = n * ((3 * n) - 1) // 2

    if len(str(i)) >= 5:
        break
    elif len(str(i)) == 4:
        table['pentagonal_nums'].append(i)

for n in range(1, maxsize ** 10):
    i = n * ((2 * n) - 1)

    if len(str(i)) >= 5:
        break
    elif len(str(i)) == 4:
        table['hexagonal_nums'].append(i)

for n in range(1, maxsize ** 10):
    i = n * ((5 * n) - 3) // 2

    if len(str(i)) >= 5:
        break
    elif len(str(i)) == 4:
        table['heptagonal_nums'].append(i)

for n in range(1, maxsize ** 10):
    i = n * ((3 * n) - 2)

    if len(str(i)) >= 5:
        break
    elif len(str(i)) == 4:
        table['octagonal_nums'].append(i)

# достаём каждое число из словоря и по ходу выполняем первое условие из задачи (ключи не должны быть равны!).
for key1 in table:
    for n1 in table[key1]:
        n1 = str(n1)
        n1_34 = n1[2:]
        n1_12 = n1[:2]

        for key2 in table:
            if key2 == key1:
                continue

            for n2 in table[key2]:
                n2 = str(n2)
                n2_34 = n2[2:]
                n2_12 = n2[:2]

                if n1_12 == n2_34:
                    for key3 in table:
                        if key3 == key2 or key3 == key1:
                            continue

                        for n3 in table[key3]:
                            n3 = str(n3)
                            n3_34 = n3[2:]
                            n3_12 = n3[:2]

                            if n2_12 == n3_34:
                                for key4 in table:
                                    if key4 == key3 or key4 == key2 or key4 == key1:
                                        continue

                                    for n4 in table[key4]:
                                        n4 = str(n4)
                                        n4_34 = n4[2:]
                                        n4_12 = n4[:2]

                                        if n3_12 == n4_34:
                                            for key5 in table:
                                                if key5 == key4 or key5 == key3 or key5 == key2 or key5 == key1:
                                                    continue

                                                for n5 in table[key5]:
                                                    n5 = str(n5)
                                                    n5_34 = n5[2:]
                                                    n5_12 = n5[:2]

                                                    if n4_12 == n5_34:
                                                        for key6 in table:
                                                            if key6 == key5 or key6 == key4 or key6 == key3 \
                                                                    or key6 == key2 or key6 == key1:
                                                                continue

                                                            for n6 in table[key6]:
                                                                n6 = str(n6)
                                                                n6_34 = n6[2:]
                                                                n6_12 = n6[:2]

                                                                if n5_12 == n6_34 and n6_12 == n1_34:
                                                                    result = [int(n1), int(n2), int(n3),
                                                                              int(n4), int(n5), int(n6)]

                                                                    print(sorted(result))
                                                                    print(sum(result))
