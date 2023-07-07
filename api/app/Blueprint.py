# coding: utf-8


# 护照模块
from app.corpus import CorpusApi
from app.upload_api import upload_api
from app.audio import AudioApi
from app.output import OutputApi

DEFAULT_BLUEPRINT = (
    # 护照模块
    (CorpusApi, '/CorpusApi'),
    (upload_api, '/upload_api'),
    (AudioApi, '/AudioApi'),
    (OutputApi, '/OutputApi')
)


def config_blueprint(app, ENV):
    """
        读取蓝图配置

        :param ENV, 运行模式, production
    """

    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix = prefix)