from itertools import count

def sqrt_(x):
    return x ** 2

def task():
    iterator_numbers = count(1, 1)
    numbers = (map(sqrt_, filter(lambda x: x % 2 == 0, iterator_numbers)))  # заменить на map и filter

    for num in range(10):  # напечатать первые 10 чисел
        print(next(numbers))  #  с помощью next получать следующий элемент от итератора


if __name__ == "__main__":
    task()
