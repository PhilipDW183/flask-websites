from flask import Blueprint

home = Blueprint("main", __name__)

from core.main import routes