from flask import Blueprint


login = Blueprint("/autenticacao", __name__)

@login.route("/login")
def login_user():
    return "login"

@login.route("/sair")
def logout():
    return "sair"