import json


def task():
    filename = "input.json"
    with open(filename) as file:
        data = json.load(file)
        #max_score = lambda x: max(x) in data[score]

    #  считать содержимое JSON файла

    return max(data, key=lambda item: item['score'])   # найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
