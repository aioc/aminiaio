from flask import Flask
from flask.ext.login import LoginManager

app = Flask('aminiaio', instance_relative_config = True)
app.config.from_pyfile('config.py')

loginManager = LoginManager(app)
@loginManager.user_loader
def loadUser(userId):
	from .db import Teacher
	try:
		return Teacher.load(int(userId))
	except Exception as e:
		print("Error loading teacher:", type(e), '-', e)
		return None

from . import login
from . import handlers