class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    def title(self):
        print(self._title)

    def author(self):
        print(self._author)

    def magazine(self):
        print(self._magazine)
pass