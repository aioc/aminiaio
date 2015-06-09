from aminiaio import app

# Error handler for invalid request type. We'll handle this by treating it as a 404.
from .error404 import error404
app.errorhandler(405)(error404)