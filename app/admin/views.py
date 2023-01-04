from flask import Blueprint

appweb = Blueprint("dash", __name__)


@appweb.route("/")
def home():
    return 