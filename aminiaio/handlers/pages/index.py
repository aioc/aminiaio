from aminiaio import app, login
from flask import render_template, request, flash
from flask.ext.login import login_user, current_user


@app.route('/', methods = ['GET', 'POST'])
def index():
	username = ''
	if request.method == 'POST':
		username = request.form.get('username', '')
		password = request.form.get('password', '')
		if not login.usernameValid(username):
			username = ''

		user = login.login(username, password)
		if user is not None:
			login_user(user, remember=True)
			flash('Welcome back %s!' % user.name(), 'alert-success')
		else:
			flash('Incorrect username or password.', 'alert-warning')

	return render_template('index.html', current_page='index', username=username, current_user=current_user)
