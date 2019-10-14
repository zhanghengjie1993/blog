from ___init__ import db


class UserInfo(db.Model):
    __tablename__ = 'user_info'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))

    def __init__(self, t_name, t_password):
        self.name = t_name
        self.password = t_password


def initdb(app):
    db.init_app(app)
    db.create_all()
