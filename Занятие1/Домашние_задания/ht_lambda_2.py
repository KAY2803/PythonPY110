#скрипт для сортировки списка кортежей по второму элементу с помощью Lambda
exam = [(1, 2), (2, 15), (4, 6), (3, 21), (12, 1)]
print(sorted(exam, key=lambda x: x[1]))

