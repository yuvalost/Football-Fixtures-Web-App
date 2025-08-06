from flask import Blueprint, jsonify, Response
import requests
from app.fetch import get_fixtures

routes = Blueprint("routes", __name__)

@routes.route("/fixtures")
def fixtures():
    try:
        data = get_fixtures()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes.route("/news")
def news():
    try:
        res = requests.get("https://www.theguardian.com/football/rss", timeout=5)
        return Response(res.content, content_type="application/xml")
    except Exception as e:
        return jsonify({"error": str(e)}), 500
