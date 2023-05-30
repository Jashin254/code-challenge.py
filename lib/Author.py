class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    def name(self):
        return self._name
    
    def articles(self):
        return self._articles
    
    def add_articles(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)  

    def magazines(self):
        unique_magazines = set()
        for article in self._articles:
            unique_magazines.add(article.magazine())
        return list(unique_magazines)
    
    def topic_areas(self):
        unique_categories = set()
        for article in self._articles:
            unique_categories.add(article.category())
        return list(unique_categories)


class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
    
    def magazine(self):
        return self._magazine
    
    def category(self):
        # Implement this method to return the category or topic area of the article
        pass


# Creating  an instance for Author
author = Author("Robert Green")


author.add_articles("48 LAWS OF POWER", "Play the fool to fool a fool")
author.add_articles("Seduction", "Mirrioring")
author.add_articles("Concise Laws of Human Nature", "Law of Aggression")

print("Author Name:", author.name())

print("Articles:", [article._title for article in author.articles()])

print("Magazines:", author.magazines())

print("Topic Areas:", author.topic_areas())
