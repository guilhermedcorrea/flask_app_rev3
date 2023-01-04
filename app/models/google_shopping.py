from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def google_db(app):
    db.init_app(app)
    app.db = db


class UrlBase(db.Model):
    __tablename__ = "urlbase"
    __bind_key__ = 'comparador'
    __table_args__ = {"schema": "precos"}

class ComparadorPreco(db.Model):
    __tablename__ = "googleprecos"
    __bind_key__ = 'comparador'
    __table_args__ = {"schema": "precos"}