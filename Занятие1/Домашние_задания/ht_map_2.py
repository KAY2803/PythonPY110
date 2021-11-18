# программа для разделения заданного словаря списков на список словарей с помощью функции map()
d = {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}

print(list(map(dict, zip(*[[(k, v) for v in value] for k, value in d.items()]))))
