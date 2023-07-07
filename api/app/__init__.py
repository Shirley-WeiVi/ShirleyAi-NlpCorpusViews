# coding: utf-8

from flask import Flask, jsonify, request
from config.runConfig import ProductionConfig
from app.Blueprint import config_blueprint
from app.Extensions import config_extensions


def create_app(ENV='production'):

    app = Flask(__name__, static_folder=ProductionConfig.static_folder)
    
    app.config.from_object(ProductionConfig)

    config_extensions(app)

    config_blueprint(app, ENV)

    @app.route("/", methods=['GET','POST'])
    def tests():
        return jsonify({
            "status":200,
            "headers": str(request.headers),
            "body": str(request.data)
        })

    return app