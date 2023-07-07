from flask import Blueprint
CorpusApi = Blueprint('CorpusApi', __name__)
from ..corpus import urls