from aminiaio import app
import psycopg2

conn = psycopg2.connect(
	database = app.config['DATABASE_NAME'],
	user     = app.config['DATABASE_USERNAME'],
	password = app.config['DATABASE_PASSWORD'],
	host     = app.config['DATABASE_HOST'],
)

# Leave this here.
conn.autocommit = True
# If not, *every* command starts a transaction that must be committed explicitly.
# This is close enough to the behaviour we want.
# ~ James

from .problem  import Problem
from .contest  import Contest
from .student  import Student
from .instance import Instance
from .teacher  import Teacher