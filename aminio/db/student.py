import random
import psycopg2

class Student(object):
	''' Represents a student for a particular contest instance. '''

    def __init__(self, username):
        self._username = username
        self._name = getQuality("name")
        self._password = getQuality("password")

    def getQuality(self, quality):
        with conn.cursor() as cur:
            cur.execute("SELECT %(qual)s FROM students WHERE username=%(me)s;", {'qual':quality, 'me':self.username()})

	@classmethod
	def usernameExists(cls, username):
        with conn.cursor() as cur:
            cur.execute("SELECT username FROM students WHERE username=%(name)s;", {'name':username})
            return cur.fetchone() != None

	@classmethod
	def create(cls, name):
		''' Get username and password, add to database. '''
        ''' Returns a Student. '''
        username = ""
        password = ""
        digits = 1
        while username == "" || Student.usernameExists(username):
            username = name.replace(" ", "").lower() + str(random.randint(10**digits, 10**(digits+1)-1))
        for i in xrange(0, 15):
            password += random.choice('abcdefghijklmnopqrstuvwxyz')
        with conn.cursor() as cur:
            cur.execute("INSERT INTO students (name, username, password) VALUES (%s, %s, %s);", (name, username, password))
        return Student(username)


	def name(self):
        return self._name

	def username(self):
        return self._username

	def password(self):
        return self._password
