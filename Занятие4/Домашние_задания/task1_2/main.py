# необходимо по отдельности вывести цитаты, которые приведены в input

import re

pattern = """(.|\n)+?"""

if __name__ == "__main__":
    def read_phrase():
        sentence_pattern = re.compile(r'(?:\"{3}(.+\n?)+?\"{3})')
        with open ('input.txt', 'r', encoding='utf-8') as file:
            for sentence in sentence_pattern.finditer(file.read()):
                print(sentence.group())
                print("---------------")

    print(read_phrase())



