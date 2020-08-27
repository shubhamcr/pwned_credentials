from flask import Blueprint

breaches_bp = Blueprint("breaches_bp", __name__)

from . import routes