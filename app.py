from flask import Flask
from controller.article_controller import ArticleController
from database import init_app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
init_app(app)

# Create an instance of the ArticleController
article_controller = ArticleController(app)

if __name__ == '__main__':
    app.run(debug=True)
