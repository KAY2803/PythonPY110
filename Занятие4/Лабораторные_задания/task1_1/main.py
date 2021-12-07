import json
import re

BOOKS_FILE = "books.md"
POSITION = r'#{4}\s?(?P<position>\b\d{1,2}\b)'
BOOK = r'(?P<book>\[(.+)?(Python)(.+)?\])'
BOOK_URL = r'(?P<book_url>http[s]?:\/\/amzn.to\/\d\w{6})'
AUTHOR = r'(?P<author>by\s+([A-Z](\.|\')?(\w+)?\s+(&)?(\s)?){2,})'
RECOMENDED = r'(?P<recommended>\b\d{1,3}.\d+%)'
COVER_URL = r'http[s]?:\/\/(?P<cover_url>[A-Za-z\d]+.+png#center\b)'
DESCRIPTION = r'(?P<description>\".+(\s)+(.+\s+.+)?\")'


def task():
    #book_pattern = re.compile(f"{POSITION}.+{BOOK}.+{BOOK_URL}.+{AUTHOR}.+{RECOMENDED}.+")
    #with open(BOOKS_FILE, 'r') as f:
        #for book in book_pattern.finditer(f.read()):
            #print(book.groupdict())
            #return book.groupdict()

    cover = re.compile(f"{COVER_URL}")
    with open(BOOKS_FILE, 'r') as f:
        for book in cover.finditer(f.read()):
            print(book.groupdict())

    #description = re.compile(f"{DESCRIPTION}")
    #with open(BOOKS_FILE, 'r') as f:
     #   for book in description.finditer(f.read()):
      #      print(book.groupdict())


if __name__ == '__main__':
    print(task())
