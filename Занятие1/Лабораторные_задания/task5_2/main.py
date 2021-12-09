from itertools import repeat

def task() -> list:
    temp_tuple = (0, 36.6, 100)

    return list(map(round, map(lambda x: x * 9/5 + 32, temp_tuple), repeat(2)))


if __name__ == "__main__":
    print(task())
