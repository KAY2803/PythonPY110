def header_footer(func):
    def wrapper():
        print("========")
        func()
        print("========")
    return wrapper
    #  написать декоратор
    ...


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
