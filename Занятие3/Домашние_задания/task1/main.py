if __name__ == "__main__":

    import json
    import random
    from string import digits, ascii_letters

    pop_1 = digits
    text_1 = random.sample(pop_1, 10)
    with open('file_1', 'w') as file_1:
        json.dump(text_1, file_1)

    pop_2 = ascii_letters
    text_2 = random.sample(pop_2, 10)
    with open('file_2', 'w') as file_2:
        json.dump(text_2, file_2)

    # запись двух списков из двух разных файлов
    file_1 = 'file_1'
    file_2 = 'file_2'
    with open(file_1, 'r') as file_1, open(file_2, 'r') as file_2, open('file_3', 'w') as file_3:
        for item in file_1:
            file_3.write(item)
            file_3.write('\n')
        for item in file_2:
            file_3.write(item)
            file_3.write('\n')
    with open('file_3', 'r') as file_3:
        for line in file_3:
            print(line)

    # объединение списков в общий и вывод на экран
    with open('file_3', 'r') as file_3:
        union_list = []
        for line in file_3:
            for item in line.strip('[]\n').split(', '):
                union_list.append(item)
        print(union_list)

    # Write your solution here
    pass
# создать файлы со списками, рандом, объединить списки и вывести на экран один общий список