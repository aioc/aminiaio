import contestinstance

class Teacher(object):
    
    def __init__(self, username):
        self._username = username
        self._instances = getQuality("instances")
        self._passhash = getQuality("passhash")


    def getQuality(self, quality):
        with conn.cursor() as cur:
            cur.execute("SELECT %(qual)s FROM problems WHERE name=%(me)s;", {'qual':quality, 'me':self.username()})
            return cur.fetchone()[0]

	@classmethod
	def login(cls, username, password):
		''' Returns a Teacher instance if the credentials are valid, or None otherwise. '''
        # assuming the password passed through can't be equal to 'None'
        with conn.cursor() as cur:
            cur.execute("SELECT passhash FROM teachers WHERE username=%s;", username)
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
        return Teacher(username)

    @classmethod
    def usernameExists(cls, username):
        with conn.cursor() as cur:
            cur.execute("SELECT username FROM teachers WHERE username = %(name)s;", {'name':username})
            return cur.fetchone() != None
            
	def save(self):
        with conn.cursor() as cur:
            cur.execute("UPDATE teachers SET passhash=%(pass)s WHERE username=%(user)s;", {'pass':self.passhash(), 'user':self.username()})
            cur.execute("UPDATE teachers SET instances=%(instances)s WHERE username=%(user)s;", {'instances':[o.instanceId() for o in self.instances()] , 'user':self.username()})

	def username(self):
        return self._username

    def instances(self):
        return self._instances

    def addInstance(self, contestid):
        self._instances += Instance.create(contestid)
        self.save()

    def delInstance(self, instanceid):
        self._instances = [o for o in self.instances() if o.instanceId != instanceid]
        self.save()

    def passhash(self):
        return self._passhash

    def setPassword(self, passhash):
        self._passhash = passhash
        self.save()
