import ConfigParser
import os

from flask import Blueprint, request

from ___init__ import db
from api import make_response_ok
from marshmallow import Schema,fields
from excption import APIException
from model import UserInfo

bp = Blueprint("auth", __name__, url_prefix='/api/auth')


class UserSchema(Schema):
    username = fields.String()
    password = fields.String()
    age = fields.String()


@bp.route("/login", methods=['POST'], endpoint='login')
def login():
    # data = request.get_json()
    # users = data["users"]
    # for user in users:
    print request.get_json()
    print request.args
    print request.form
    username = request.form.get('username')
    password = request.form.get('password')
    # user = db.session.query(UserInfo).filter(UserInfo.name == username).first()
    # if user is None or user.password != password:
    #     raise APIException(1, "user not exist")
    # else:
    try:
        file = request.files['file']
    except Exception:
        print 'error'
        raise Exception('this is')
    if file is None:
        print 'file cant none'
    print file.filename
    file.save(os.path.join('C:\\Users\\zhanghengjie\\PycharmProjects\\blog\\api', file.filename))
    db.session.add(UserInfo(username, password))
    db.session.commit()
    return make_response_ok()




