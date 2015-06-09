from aminiaio import app

# Error handler for bad authentication. We'll handle this by treating it as a 404.
from .error404 import error404
app.errorhandler(401)(error404)