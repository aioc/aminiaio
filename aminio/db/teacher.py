# Teacher model

class Teacher(object):
    
    def __init__(self, username):
        self._username = username
        self._instances = getQuality("instances")


    def getQuality(self, quality):
        with conn.cursor() as cur:
            cur.execute("SELECT %(qual)s FROM problems WHERE name='%(me)s';", {'qual':quality, 'me':self.username()})
            return cur.fetchone()[0]

	@classmethod
	def login(cls, username, password):
		''' Returns a Teacher instance if the credentials are valid, or None otherwise. '''
        # assuming the password passed through can't be equal to 'None'
        with conn.cursor() as cur:
            cur.execute("SELECT passhash FROM teachers WHERE username='%s';", username)
            passhash = cur.fetchone()[]
        if password != passhash or password == None:
            return None
        return Teacher(username)

    @classmethod
    def create(cls, username, password):
        if Teacher.usernameExists(username):
            return None
#TODO: some sort of error b/c duplicate username?
        with conn.cursor() as cur:
            cur.execute("INSERT INTO teachers (username, passhash, instances) VALUES (%s, %s, %s);", (username, password, []))
        return Student(username)

    @classmethod
    def usernameExists(cls, username):
        with conn.cursor() as cur:
            cur.execute("SELECT username FROM teachers WHERE username = '%(name)s';", {'name':username})
            return cur.fetchone() != None
            
        
	def save(self):
		raise NotImplemented

	def username(self):
        return self._username

    def instances(self):
        return self._instances

	# contest instances and manipulation


