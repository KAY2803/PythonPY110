if __name__ == "__main__":
    def decor_int(fn):
        def wrapper(*args):
            for x in args:
                if not isinstance(x, int):
                    raise ValueError ("Не все аргументы числа")
            return fn(*args)
        return wrapper

@decor_int
def func_test(*args):
    return args

print(func_test(1, 'adf', 3, 4))

