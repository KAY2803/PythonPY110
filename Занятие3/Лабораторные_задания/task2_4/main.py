import json


def task():
    filename = "input.json"
    with open(filename) as file:
       data = json.load(file)
    #  считать содержимое JSON файла

    gen_exr = (item["contains_improvement_appeals"] for item in data)
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
