INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE, 'r') as file:  #  открыть указатель на файл
        for line in file:
            print(line, end='')
        ...  #  файл является итератором, который работает с циклом for в построчном режиме


if __name__ == "__main__":
    task()
