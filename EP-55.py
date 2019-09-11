'''Задача 55'''
# Если взять число 47, перевернуть его и прибавить к исходному, т.е. найти 47 + 74 = 121, получится палиндром.
# Не из всех чисел таким образом сразу получается палиндром. К примеру,
# 349 + 943 = 1292
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
# Т.е., понадобилось 3 итерации для того, чтобы превратить число 349 в палиндром.
# Хотя никто еще этого не доказал, считается, что из некоторых чисел, таких как 196, невозможно получить палиндром.
# Такое число, которое не образует палиндром путем переворачивания и сложения с самим собой, называется числом Личрэла.
# Ввиду теоретической природы таких чисел, а также цели этой задачи, мы будем считать, что число является числом Личрэла
# до тех пор, пока не будет доказано обратное. Помимо этого дано, что любое число меньше десяти тысяч либо (1)
# станет палиндромом меньше, чем за 50 итераций, либо (2) никто, с какой бы-то ни было вычислительной мощностью,
# не смог получить из него палиндром. Между прочим, 10677 является первым числом, для которого необходимо более 50
# итераций, чтобы получить палиндром: 4668731596684224866951378664 (53 итерации, 28-значное число).
# На удивление, есть такие палиндромы, которые одновременно являются и числами Личрэла; первое такое число - 4994.
# Сколько существует чисел Личрэла меньше десяти тысяч?
# ПРИМЕЧАНИЕ: Формулировка задачи была немного изменена 24 апреля 2007 года, чтобы подчеркнуть теоретическую природу
# чисел Личрэла.

result = 0
iterations = 50

for num in range(10, 10000):
    iterations_number = 0

    while True:
        turn_num = str(num)[::-1]
        sum_nums = num + int(turn_num)
        iterations_number += 1

        if sum_nums == int(str(sum_nums)[::-1]):
            break

        else:
            num = sum_nums

            if iterations_number >= iterations:
                result += 1
                break

print(result)


