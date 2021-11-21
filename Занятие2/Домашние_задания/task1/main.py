
if __name__ == "__main__":
    def geo_gen(start_number, k: int):
        while True:
            yield start_number
            start_number *= k

    my_count = geo_gen(1, 3)
    for _ in range(10):
        print(next(my_count))

    # Write your solution here
    pass
