from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    """
    产生app实例:
        实例化
        加载配置
        加载扩展

        注册各类路由

    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # enable CORS
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # 注册蓝图
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app

from app import models

