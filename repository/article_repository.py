from domain.article import Article
from database import db

class ArticleRepository:
    def add_article(self, article):
        db.session.add(article)
        db.session.commit()

    def get_articles(self):
        return Article.query.all()
