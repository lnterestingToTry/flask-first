from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask_first'

db = SQLAlchemy(app)


login_mananger = LoginManager()
login_mananger.login_view = 'auth.login'
login_mananger.init_app(app)

from .models import Users, Notes

@login_mananger.user_loader
def load_user(id):
    return Users.query.get(int(id))


from .views import views
from .auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')


with app.app_context():
    db.create_all()