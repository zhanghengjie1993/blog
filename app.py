from ___init__ import app
from api import auth
from config import Config
from model import initdb

app.config.from_object(Config)
app.register_blueprint(auth.bp)
initdb(app)


if __name__ == '__main__':
    app.run()
