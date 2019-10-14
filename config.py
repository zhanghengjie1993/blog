# coding:utf8
import os


class Config:
    SECRET_KEY = os.urandom (24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True



    @staticmethod
    def init_app(app):
        pass
