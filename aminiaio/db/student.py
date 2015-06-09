from . import conn
import random

class Student(object):
	''' Represents a student for a particular contest instance. '''

	def __init__(self, studentId, name, username=None, password=None):
		self._studentId = studentId
		self._name = name
		self._username = username
		self._password = password

	@classmethod
	def _usernameExists(cls, username):
		with conn.cursor() as cur:
			cur.execute('SELECT username FROM students WHERE username = %s;', (username,))
			return cur.fetchone() != None

	@classmethod
	def load(cls, studentId):
		with conn.cursor() as cur:
			cur.execute('SELECT name, username, password FROM students WHERE student_id=%s;', (studentId,))
			result = cur.fetchone()
			if result is None:
				return None
			name, username, password = result
			return cls(studentId, name, username, password)

	def _save(self):
		''' Updates the database record for this Student with the current name, username, and password. '''
		with conn.cursor() as cur:
			cur.execute(
				'UPDATE students SET name=%(name)s, username=%(username)s, password=%(password)s WHERE student_id=%(studentId)s;',
				{
					'studentId': self.studentId(),
					'name': self.name(),
					'username': self.username(),
					'password': self.password(),
				}
			)
			return self

	@classmethod
	def create(cls, name):
		''' Creates and returns a new Student with the specified name. '''
		with conn.cursor() as cur:
			cur.execute('INSERT INTO students (name) VALUES (%s) RETURNING student_id;', (name,))
			studentId, = cur.fetchone()
			return cls.load(studentId)

	

	def delete(self):
		''' Removes the corresponding database record for this Student. '''
		with conn.cursor() as cur:
			cur.execute('DELETE FROM students WHERE student_id=%s;', (self.studentId(),))
			self._studentId = None

	def generateCredentials(self):
		''' Assigns this student a username and password. '''

		username = '_'.join(''.join(c for c in part.lower() if 'a' <= c <= 'z') for part in self.name().split())
		while cls.usernameExists(username):
			username += str(random.randint(0,9))

		# Birthday paradox: expect a duplicate password in a group of N students if we have < N^2 passwords.
		# This is good for a group of 50 students (>10000 possibilities)
		# Maybe you just want 4 numbers ~shrug~
		# ~ James
		password = \
			random.choice('cute amazing awesome this the interesting convincing good bad evil nice talking'.split()) + \
			random.choice('password wombat word thing banana apple cat koala walrus budgie problem'.split()) + \
			str(random.randint(0,9)) + \
			str(random.randint(0,9))

		return self._save()

	def setName(self, name):
		self._name = name
		return self._save()

	def studentId(self):
		return self._studentId

	def name(self):
		return self._name

	def username(self):
		return self._username

	def password(self):
		return self._password
