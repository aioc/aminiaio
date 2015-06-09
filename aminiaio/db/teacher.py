from . import conn, Instance
from flask.ext.login import UserMixin # Provides standard implementations of flask.login requirements
import hashlib

def _hash(string):
	return hashlib.sha256(repr(string).encode('utf-8')).hexdigest()

class Teacher(UserMixin):
	
	def __init__(self, teacherId, username, passhash, instances):
		self._teacherId = teacherId
		self._username = username
		self._passhash = passhash
		self._instances = list(instances)

	@classmethod
	def load(cls, teacherId):
		with conn.cursor() as cur:
			cur.execute('SELECT username, passhash, instances FROM teachers WHERE teacher_id = %s;', (teacherId,))
			result = cur.fetchone()
			if result is None:
				return None
			username, passhash, instances = result
			return cls(teacherId, username, passhash, instances)

	@classmethod
	def _usernameExists(cls, username):
		with conn.cursor() as cur:
			cur.execute("SELECT username FROM teachers WHERE username = %s;", (username,))
			return cur.fetchone() != None

	@classmethod
	def _getPasshash(cls, username, password):
		return _hash(_hash(username) + password)

	def _hashPassword(self, password):
		return type(self)._getPasshash(self._username, password)

	def passwordValid(self, password):
		return self._hashPassword(password) == self._passhash

	@classmethod
	def create(cls, username, password):
		if cls._usernameExists(username):
			return None
		with conn.cursor() as cur:
			cur.execute('''
				INSERT INTO teachers (username, passhash, instances)
				VALUES (%(username)s, %(passhash)s, %(instances)s)
				RETURNING teacher_id;
				''',
				{
					'username': username,
					'passhash': cls._getPasshash(username, password),
					'instances': [],
				}
			)
			teacherId, = cur.fetchone()
			return cls.load(teacherId)

	@classmethod
	def login(cls, username, password):
		''' Returns a Teacher instance if the credentials are valid, or None otherwise. '''
		with conn.cursor() as cur:
			cur.execute('SELECT teacher_id, passhash FROM teachers WHERE username=%s;', (username,))
			result = cur.fetchone()
			if result is None:
				return None
			teacherId, passhash = result
			return None if cls._getPasshash(username, password) != passhash else cls.load(teacherId)

	def _save(self):
		with conn.cursor() as cur:
			cur.execute(
				'UPDATE teachers SET passhash=%(passhash)s, instances=%(instances)s WHERE username=%(user)s;',
				{
					'passhash': self.passhash(),
					'instances': self.instances(),
				}
			)
		return self


	def teacherId(self):
		return self._teacherId

	def username(self):
		return self._username

	def name(self):
		return self.username()

	def instances(self):
		return tuple(self._instances)

	def createInstance(self, contestId):
		instance = Instance.create(contestId)
		if instance is None:
			raise ValueError("Invalid contest id.")
		self._instances.append(instance)
		return self._save()

	def removeInstance(self, instance):
		self._instances.remove(instance)
		return self._save()

	def setPassword(self, password):
		self._passhash = self._hashPassword(password)
		return self._save()


	# For flask.login:
	def get_id(self):
		return str(self.teacherId())
