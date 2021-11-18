# скрипт, чтобы найти максимальное значение в заданном неоднородном списке с помощью лямбда
exam = ['Python', 3, 2, 4, 5, 'version']
max_x = max(map(lambda x: x if isinstance(x, int) else not x, exam))
print(max_x)

