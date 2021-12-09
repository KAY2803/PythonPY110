if __name__ == "__main__":
    def decor_check_iter(fn):
        def wrapper(*args, **kwargs):
            for arg in args:
                try:
                    _ = (a for a in arg)
                except TypeError:
                    raise TypeError({f'Объект {arg} не является итерируемым'})
            for kwarg in kwargs:
                try:
                    _ = (k for k in kwarg)
                except TypeError:
                    print({f'Объект {kwarg} не является итерируемым'})
            return fn(*args, **kwargs)
        return wrapper

@decor_check_iter
def func_iter(*args, **kwargs):
    return args, kwargs

b = [1, 2, 3]
print(func_iter(3, 7, 'f', 9, b, k=3))