def task(camel_case_str: str) -> str:
    return "".join(filter(str.islower, word))


if __name__ == "__main__":
    word = "AbCdEfGh"
    print(task(word))
