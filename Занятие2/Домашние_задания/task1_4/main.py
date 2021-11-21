def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i+1]


def task():
    for pair in pairwise("ABCDEFG"):
        print(pair)


if __name__ == "__main__":
   # task()

    # Другой вариант
    def pairwise_1(it):
        pair = (it[x] + it[x+1] for x in range(len(it)-1))
        return list(pair)

    print(pairwise_1("ABCDEFG"))