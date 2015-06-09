from aminiaio import app
from flask import redirect, flash
from flask.ext.login import current_user, logout_user, login_required


@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('Successfully logged out.', 'alert-info')
	return redirect('/')
