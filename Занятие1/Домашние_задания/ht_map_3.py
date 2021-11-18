list_1 = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
list_2 = [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]

print(list(map(' '.join, list_1)))
print(list(map(' '.join, list_2)))