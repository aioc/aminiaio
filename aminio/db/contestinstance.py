import student

class ContestInstance(object):
    
    def __init__(self, instanceid):
        self._instanceId = instanceid
        self._contestid = getQuality("contestid")
        self._students = getQuality("students")
        self._launched = getQuality("launched")

    def getQuality(self, quality):
        with conn.cursor() as cur:
            cur.execute("SELECT %(qual)s FROM instances WHERE name=%(me)s;", {'qual':quality, 'me':self.problemName()})
            return cur.fetchone()[0]

    @classmethod
    def create(cls, contestid):
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM instances ORDER BY id DESC LIMIT 1")
            instanceid = cur.fetchone()[0]+1
            cur.execute("INSERT INTO instances VALUES (%(instanceid)s, %(contestid)s, [], %(launched)s);", {'instanceid':instanceid, 'contestid':contestid, 'launched':False})
        return ContestInstance.(instanceid)
    
    def instanceId(self):
        return self._instanceId

	def contestId(self):
        return self._contestid

	def students(self):
        return self._students

	def launched(self):
        return self._launched

    def setContestId(self, newid):
        self._contestid = newid

    def addStudent(self, name):
        self._students += Student(name)
        self.save()

    def deleteStudent(self, studentUsername):
        self._students = [o for o in self.students() if o.username() != studentUsername]
        self.save()

    def save(self):
        with conn.cursor() as cur:
            cur.execute("UPDATE instances SET students = %(stud)s WHERE id=%(myId)s;", {"myId":self.contestId(), "stud":[o.username() for o in self.students()]})
