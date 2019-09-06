'''Задача 44'''
# Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2. Первые десять пятиугольных чисел:
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
# Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8. Однако, их разность, 70 − 22 = 48,
# не является пятиугольным числом.
# Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность являются пятиугольными
# числами и значение D = |Pk − Pj| минимально, и дайте значение D в качестве ответа.

from math import floor

result = []  # Время работы 2мин 42с
lst = []
a = 0
min_ = 1
max_ = 5000


def func(arg1, arg2):  # Находит разность
    sub_ = arg2 - arg1
    midd = floor((min_ + max_) / 2)

    if sub_ == lst[midd]:
        return result.append(sub_)

    elif sub_ > lst[midd]:
        mid_bb = floor((midd + max_) / 2)

        if lst[mid_bb] == sub_:
            return result.append(sub_)

        elif sub_ > lst[mid_bb]:
            if sub_ in lst[mid_bb:max_]:
                return result.append(sub_)

        else:
            if sub_ in lst[midd:mid_bb]:
                return result.append(sub_)

    else:
        mid_ss = floor((midd + min_) / 2)

        if lst[mid_ss] == sub_:
            return result.append(sub_)

        elif sub_ > lst[mid_ss]:
            if sub_ in lst[mid_ss:midd]:
                return result.append(sub_)

        else:
            if sub_ in lst[min_:mid_ss]:
                return result.append(sub_)


for n in range(1, max_ + 1):
    lst.append(int((n * ((3 * n) - 1)) / 2))


for i in lst:
    a += 1
    print(i)

    for j in lst[a:]:
        sum_ = i + j
        mid = int(floor((a + max_) / 2))  # для ускорения работы делим список на части

        if sum_ == lst[mid]:
            func(i, j)
            continue

        elif sum_ > lst[mid]:
            mid_b = floor((mid + max_) / 2)  # для ускорения работы делим список на части

            if lst[mid_b] == sum_:
                func(i, j)
                continue

            elif sum_ > lst[mid_b]:
                mid_bb = floor((mid_b + max_) / 2)  # для ускорения работы делим список на части

                if lst[mid_bb] == sum_:
                    func(i, j)
                    continue

                elif sum_ > lst[mid_bb]:
                    if sum_ in lst[mid_bb:max_]:
                        func(i, j)
                        continue

                else:
                    if sum_ in lst[mid_b:mid_bb]:
                        func(i, j)
                        continue

            else:
                mid_bs = floor((mid + mid_b) / 2)  # для ускорения работы делим список на части

                if lst[mid_bs] == sum_:
                    func(i, j)
                    continue

                elif sum_ > lst[mid_bs]:
                    if sum_ in lst[mid_bs:mid_b]:
                        func(i, j)
                        continue

                else:
                    if sum_ in lst[mid:mid_bs]:
                        func(i, j)
                        continue

        else:
            mid_s = floor((mid + a) / 2)  # для ускорения работы делим список на части

            if lst[mid_s] == sum_:
                func(i, j)
                continue

            elif sum_ > lst[mid_s]:
                mid_sb = floor((mid + mid_s) / 2)  # для ускорения работы делим список на части

                if lst[mid_sb] == sum_:
                    func(i, j)
                    continue

                elif sum_ > lst[mid_sb]:
                    if sum_ in lst[mid_sb:mid]:
                        func(i, j)
                        continue

                else:
                    if sum_ in lst[mid_s:mid_sb]:
                        func(i, j)
                        continue

            else:
                mid_ss = floor((a + mid_s) / 2)  # для ускорения работы делим список на части

                if lst[mid_ss] == sum_:
                    func(i, j)
                    continue

                elif sum_ > lst[mid_ss]:
                    if sum_ in lst[mid_ss:mid_s]:
                        func(i, j)
                        continue

                else:
                    if sum_ in lst[a:mid_ss]:
                        func(i, j)
                        continue

print('result:', result)

