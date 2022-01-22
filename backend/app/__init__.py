from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_bootstrap import Bootstrap
from flask_mail import Mail

app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object(Config)
mail = Mail(app)
db = SQLAlchemy(app)
if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
    migrate = Migrate(app, db, render_as_batch=True)
else:
    migrate = Migrate(app, db, render_as_batch=False)


from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app import routes, models, errors
bootstrap = Bootstrap(app)



def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)
    mail = Mail(app)
    db = SQLAlchemy(app)
    if app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite"):
        migrate = Migrate(app, db, render_as_batch=True)
    else:
        migrate = Migrate(app, db, render_as_batch=False)
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    from app import routes, models, errors
    bootstrap = Bootstrap(app)
    return app
