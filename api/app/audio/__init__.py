from flask import Blueprint
AudioApi = Blueprint('AudioApi', __name__)
from ..audio import urls