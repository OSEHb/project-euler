'''Задача 58'''
# Начиная с 1 и продвигаясь по спирали в направлении против часовой стрелки,
# получается квадратная спираль с длиной стороны 7

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# Интересно заметить, что нечетные квадраты лежат на правой нижней полудиагонали. Еще интереснее то,
# что среди 13 чисел, лежащих на обеих диагоналях, 8 являются простыми; т.е. отношение составляет 8/13 ≈ 62%.
# Если добавить еще один целый слой вокруг изображенной выше спирали, получится квадратная спираль с длиной стороны 9.
# Если продолжать данный процесс, какой будет длина стороны квадратной спирали, у которой отношение количества
# простых чисел к количеству всех чисел на обеих диагоналях упадет ниже 10%?

from math import sqrt, floor

nums_in_diagonal = [1, 3, 5, 7, 9, ]
prime_num = []
check = [1, ]
num = 9
right = 4
up = 4
left = 4
down = 4
percent = 100


def func(arg):
    for i in arg:
        for j in range(1, i + 1, 2):
            if j > int(floor(sqrt(i) + 1)):
                prime_num.append(i)
                check.append(i)
                break
            elif i % j == 0 and j != 1:
                check.append(i)
                break

    return len(prime_num) * 100 / len(nums_in_diagonal)


while True:
    num += up
    nums_in_diagonal.append(num)
    num += left
    nums_in_diagonal.append(num)
    num += down
    nums_in_diagonal.append(num)
    num += right
    nums_in_diagonal.append(num)

    percent = func(set(nums_in_diagonal) - set(check))
    if percent > 10:
        right += 2
        up += 2
        left += 2
        down += 2
        print(percent, '%')
    else:
        print('result:', right + 1)
        break


