import student

class ContestInstance(object):
    
    def __init__(self, instanceid):
        self._instanceId = instanceid
        self._contestid = None
        self._students = []
        self._launched = False

    def getQuality(self, quality):
        with conn.cursor() as cur:
            cur.execute("SELECT %(qual)s FROM instances WHERE name='%(me)s';", {'qual':quality, 'me':self.problemName()})
            return cur.fetchone()[0]

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
        self.updateStudentListinDB()

    def deleteStudent(self, studentUsername):
        self._students = [o for o in self.students() if o.username() != studentUsername]
        self.updateStudentListinDB()
    
    def updateStudentListinDB(self):
        with conn.cursor() as cur:
            cur.execute("UPDATE instances SET students = %(stud)s WHERE id=%(myId)s;", {"myId":self.contestId(), "stud":[o.username() for o in self.students()]})
