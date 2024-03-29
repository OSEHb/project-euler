'''Задача 27.'''
# Эйлер опубликовал свою замечательную квадратичную формулу:
# n2+n+41
# Оказалось, что согласно данной формуле можно получить 40 простых чисел, последовательно подставляя значения 0≤n≤39.
# Однако, при n=40, 402+40+41=40(40+1)+41 делится на 41 без остатка, и, очевидно,
# при n=41,412+41+41 делится на 41 без остатка.
# При помощи компьютеров была найдена невероятная формула n2−79n+1601,
# согласно которой можно получить 80 простых чисел для последовательных значений n от 0 до 79.
# Произведение коэффициентов −79 и 1601 равно −126479.
# Рассмотрим квадратичную формулу вида:
# n2+an+b, где |a|<1000 и |b|≤1000
# где |n| является модулем (абсолютным значением) n.
# К примеру, |11|=11 и |−4|=4
# Найдите произведение коэффициентов a и b квадратичного выражения,
# согласно которому можно получить максимальное количество простых чисел для последовательных значений n,
# начиная со значения n=0.


from sys import maxsize

result = 0
result_a = 0
result_b = 0
a = -999

while True:
    if a == 1000:
        break
    for b in range(-1000, 1001):
        nums = 0
        for n in range(0, maxsize ** 10):
            div = 0
            sq = (n ** 2) + (a * n) + b
            sq = abs(sq)
            if sq % 2 == 0:
                break
            for i in range(3, sq, 2):
                if sq % i == 0:
                    div += 1
                    break
            if div > 0:
                break
            elif div == 0:
                nums += 1
        if nums > result:
            result = nums
            result_a = a
            result_b = b
    a += 1
    print(a)

print('a:', result_a)
print('b:', result_b)
print('result = ', result_a * result_b)

