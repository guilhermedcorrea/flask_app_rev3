from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def user_db(app):
    db.init_app(app)
    app.db = db

class Usuarios(db.Model):
    __tablename__ = "usuarios"
    __bind_key__ = 'permissoes'
    __table_args__ = {"schema": "acessos"}
    idusuario = db.Column(db.Integer)
    nomeusuario = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    grupo_usuario = db.Column(db.String)
    usuario_ativo = db.Column(db.String)
    datacadastro = db.Column(db.DateTime, unique=False, nullable=False)
    data_login = db.Column(db.String)

class GrupoUsuarios:
    __tablename__ = "grupos"
    __bind_key__ = 'permissoes'
    __table_args__ = {"schema": "acessos"}
    idgrupo = db.Column(db.Integer, primary_key=True)
    grupo = db.Column(db.String)
    data_cadastro = db.Column(db.DateTime, unique=False, nullable=False)

class LogUsuarios:
    __tablename__ = "logusuarios"
    __bind_key__ = 'permissoes'
    __table_args__ = {"schema": "acessos"}
    idlog = db.Column(db.Integer, primary_key=True)
    data_logado = db.Column(db.DateTime, unique=False, nullable=False)
    dia_logado = db.Column(db.String)
    hora_logado = db.Column(db.String)
    visualizacao = db.Column(db.String)
    tempo_visualizacao = db.Column(db.String)
    idusuario = db.Column(db.Integer)
    id_grupo = db.Column(db.Integer)



    

