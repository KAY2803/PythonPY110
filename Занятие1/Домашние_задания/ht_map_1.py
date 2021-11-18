values = ['U', 'f', 'a', 'b', 'i', 'o', 'E', 'i']
a = map(str.upper, set(values))
b = map(str.lower, set(values))
print(tuple(zip(a, b)))
