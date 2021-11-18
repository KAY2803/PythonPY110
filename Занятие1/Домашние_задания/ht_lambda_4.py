#скрипт для сложения двух заданных списков, используя map и lambda

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
print(sum(map((lambda x, y: x + y), list_1, list_2)))
