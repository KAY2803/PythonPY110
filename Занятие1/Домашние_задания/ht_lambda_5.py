palin = ['шалаш', 'еда', 'палас', 'кино', 'кок']
print(list(filter((lambda x: x[::] == x[::-1]), palin)))
