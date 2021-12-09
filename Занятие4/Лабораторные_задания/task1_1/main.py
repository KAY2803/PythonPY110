import json
import re
from operator import itemgetter

# создаем регулярные выражения и присваиваем их переменным
BOOKS_FILE = "books.md"
POSITION = r'#{4}\s?(?P<position>\b\d{1,2}\b)'
NAME = r'(?P<book>\[(.+)?(Python)(.+)?\])'
BOOK_URL = r'(?P<book_url>http[s]?:\/\/amzn.to\/\d\w{6})'
AUTHOR = r'(?P<author>by\s+([A-Z](\.|\')?(\w+)?\s+(&)?(\s)?){2,})'
RECOMENDED = r'(?P<recommended>\b\d{1,3}.\d+%)'
COVER_URL = r'http[s]?:\/\/(?P<cover_url>[A-Za-z\d]+.+png#center\b)'
DESCRIPTION = r'(?P<description>\".+(\s)+(.+\s+.+)?\")'

def task():
    # обрабатываем регулярные выражения для дальнейшего создания списка словарей
    # по соответствующему регулярному выражению
    position_pattern = re.compile(POSITION)
    name_pattern = re.compile(NAME)
    book_url_pattern = re.compile(BOOK_URL)
    author_pattern = re.compile(AUTHOR)
    recommend_pattern = re.compile(RECOMENDED)
    cover_pattern = re.compile(COVER_URL)
    description_pattern = re.compile(DESCRIPTION)

    # создаем списки словарей по регулярным выражениям
    with open(BOOKS_FILE, 'r') as f:
        text = f.read()
        book_list = []
        for book in position_pattern.finditer(text):
            book_list.append(book.groupdict())
        name_list = []
        for book in name_pattern.finditer(text):
            name_list.append(book.groupdict())
        book_url_list = []
        for book in book_url_pattern.finditer(text):
            book_url_list.append(book.groupdict())
        author_list = []
        for book in author_pattern.finditer(text):
            author_list.append(book.groupdict())
        recommend_list = []
        for book in recommend_pattern.finditer(text):
            recommend_list.append(book.groupdict())
        cover_list = []
        for book in cover_pattern.finditer(text):
            cover_list.append(book.groupdict())
        description_list = []
        for book in description_pattern.finditer(text):
            description_list.append(book.groupdict())
        # объединяем словари
        index = 0
        for book in book_list:
            book.update(name_list[index])
            book.update(book_url_list[index])
            book.update(author_list[index])
            book.update(recommend_list[index])
            book.update(cover_list[index])
            book.update(description_list[index])
            index += 1
        return book_list


if __name__ == '__main__':

    # переводим значение ключа 'recommended' из str в int для последующей сортировки по данному значению
    def book_list_int():
        book_list_int = task()
        for book in book_list_int:
            for key, value in book.items():
                if key == 'recommended':
                    value = float(value.rstrip('%'))
                    book['recommended'] = value
            continue
        return book_list_int


    # сортируем словари по значению ключа 'recommended' и кодируем в json файл
    def json_file():
        sort_dict = sorted(book_list_int(), key=itemgetter('recommended'), reverse=True)
        json_file = json.dumps(sort_dict, indent=4)
        return json_file
    print(json_file())

