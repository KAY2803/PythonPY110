def min_len_check(fn):
    def wrapper(arg):
        if len(arg) < 10:
            raise ValueError ("Строка слишком короткая")
        # result
        return fn(arg)
    #  записать обертку для исходной функции

    return wrapper


#  задекорировать функцию
@min_len_check
def some_func(str_arg: str):
    print(str_arg)


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
