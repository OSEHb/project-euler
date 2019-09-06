'''Задача 39.'''
# Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c},
# то существует ровно три решения для p = 120:
# {20,48,52}, {24,45,51}, {30,40,50}
# Какое значение p ≤ 1000 дает максимальное число решений?

result = []
p_result = 1
len_result = []
p = 1

while p <= 1000:  # Время работы 2,5 мин
    for a in range(1, p + 1):
        for b in range(a, p + 1):
            if a + b > p:
                break

            c = p - (a + b)

            if a ** 2 + b ** 2 == c ** 2:
                abc = (a, b, c)
                len_result.append(abc)

    if len(len_result) > len(result):
        result = len_result
        p_result = p
        len_result = []
        print('p=', p_result, 'len:', len(result), result)

    else:
        len_result = []

    p += 1

print('result:', p_result)
