from string import ascii_lowercase, ascii_uppercase, digits
import random

def gen_ran():
    pop = ascii_lowercase + ascii_uppercase + digits
    gen = (random.sample(pop, 8))
    return gen

if __name__ == "__main__":
    print(ascii_lowercase)
    print(ascii_uppercase)
    print(digits)
    print(gen_ran())
