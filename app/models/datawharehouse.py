from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def dw_db(app):
    db.init_app(app)
    app.db = db
