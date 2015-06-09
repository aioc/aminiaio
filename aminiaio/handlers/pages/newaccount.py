from aminiaio import app
from aminiaio import login
from flask import redirect, request, flash
from flask.ext.login import current_user, login_user


@app.route('/newaccount', methods=['POST'])
def newaccount():
	if current_user.is_authenticated():
		abort(404)

	username = request.form.get('username', '')
	password = request.form.get('password', '')
	invalidCredentials = False

	if not login.usernameValid(username):
		invalidCredentials = True
		flash('Invalid username. ' + login.usernameDescription(), 'alert-danger')

	if not login.passwordValid(password):
		invalidCredentials = True
		flash('Invalid password. ' + login.passwordDescription(), 'alert-danger')

	if not invalidCredentials:
		user = login.create(username, password)
		if user is None:
			flash('Username is already in use.  Please log in or choose a different username.', 'alert-warning')
		else:
			login_user(user)
			flash('Account created successfully.  Welcome %s!' % user.name(), 'alert-success')

	return redirect('/')
	


