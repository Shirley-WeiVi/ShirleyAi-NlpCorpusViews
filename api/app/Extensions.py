# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def config_extensions(app):
    """
        初始化引入库:init_app
    """

    CORS(app, supports_credentials=True)

    db.init_app(app)