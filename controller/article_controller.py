from flask import request, jsonify
from service.article_service import ArticleService


class ArticleController:
    def __init__(self, app):
        self.app = app
        self.article_service = ArticleService()

        self.app.add_url_rule('/articles', view_func=self.get_articles, methods=['GET'])
        self.app.add_url_rule('/articles', view_func=self.post_article, methods=['POST'])
        self.app.add_url_rule('/get_articles', view_func=self.get_articles, methods=['GET'])
        self.app.add_url_rule('/post_articles', view_func=self.post_article, methods=['POST'])

    def get_articles(self):
        articles = self.article_service.get_articles()
        return jsonify([article.to_dict() for article in articles])

    def post_article(self):
        data = request.get_json()
        title = data['title']
        content = data['content']
        user_id = data['user_id']
        self.article_service.add_article(title, content, user_id)
        return jsonify({'message': 'Article posted successfully'})
