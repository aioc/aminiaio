from aminiaio import app
from flask import flash, redirect

@app.errorhandler(404)
def error404(error):
	flash('We couldn\'t find anything at that location - redirected you home.', 'alert-warning')
	return redirect('/')
