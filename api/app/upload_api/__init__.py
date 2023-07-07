from flask import Blueprint
upload_api = Blueprint('upload_api', __name__)
from ..upload_api import urls

