# Cкрипт с использованием лямбда-выражения, чтобы проверить, отсортирован ли указанный список
exam = [3, 7, 4, 9, 15, 2]
exam_1 = [1, 2, 3, 4, 5]

check = lambda x: True if x == sorted(x) else False
print(check(exam))
print(check(exam_1))
