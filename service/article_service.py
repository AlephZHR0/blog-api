from domain.article import Article
from repository.article_repository import ArticleRepository


class ArticleService:
    def __init__(self):
        self.repository = ArticleRepository()

    def add_article(self, title, content, user_id):
        article = Article(title, content, user_id)
        self.repository.add_article(article)


    def get_articles(self):
        return self.repository.get_articles()
