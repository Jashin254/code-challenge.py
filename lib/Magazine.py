from Article import Article

class Magazine:
    magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.magazines.append(self)
        self._articles = []

    def name(self):
        print(self._name)

    def category(self):
        print(self._category)

    def all(self):
        print(Magazine.magazines)

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)

    def contributors(self):
        print(list(set([article.author() for article in self._articles])))

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.magazines:
            if magazine.name() == name:
                print(magazine)
        return None

    @classmethod
    def article_titles(cls):
        titles = []
        for magazine in cls.magazines:
            for article in magazine._articles:
                titles.append(article.title())
        print(titles)

    def contributing_authors(self):
        authors = []
        for author in self.contributors():
            if sum([1 for article in author.articles() if article.magazine() == self]) > 2:
                authors.append(author)
        print(authors)
pass