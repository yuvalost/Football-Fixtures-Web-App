from flask import Blueprint, jsonify
from .fetch import get_fixtures

bp = Blueprint('routes', __name__)

@bp.route("/fixtures", methods=["GET"])
def fixtures():
    return jsonify(get_fixtures())
