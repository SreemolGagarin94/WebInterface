
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

csrf = CSRFProtect()

#login_manager.init_app(app)
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


csrf.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/smsDb'
app.config['SECRET_KEY'] = 'b4ee24599aa4b85b418755c1'
db = SQLAlchemy(app)

from WebInterface import application