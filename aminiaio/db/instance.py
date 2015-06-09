from . import conn, Student

# TODO: Convert to use Contests instead of contestIds?

class Instance(object):
	
	def __init__(self, instanceId, contestId, students, launched):
		self._instanceId = instanceId
		self._contestId = contestId
		self._students = list(students)
		self._launched = launched

	@classmethod
	def load(cls, instanceId):
		with conn.cursor() as cur:
			cur.execute('SELECT contest_id, student_ids, launched FROM instances WHERE instance_id=%s;', (instanceId,))
			result = cur.fetchone()
			if result is None:
				return None
			contestId, studentIds, launched = result
			return cls(instanceId, contestId, map(Student.load, studentIds), launched)

	@classmethod
	def create(cls, contestId):
		with conn.cursor() as cur:
			cur.execute(
				'INSERT INTO instances (contest_id, student_ids, launched) VALUES (%s, [], FALSE) RETURNING instance_id;',
				(contestId,)
			)
			instanceId, = cur.fetchone()
			return cls.load(instanceId)

	def _save(self):
		with conn.cursor() as cur:
			cur.execute('''
				UPDATE instances SET contest_id=%(contestId)s, student_ids = %(studentIds)s, lauched = %(launched)s
				WHERE instance_id=%(instanceId)s;
				''',
				{
					'instanceId': self.instanceId(),
					'contestId': self.contestId(),
					'launched': self.launched(),
					'studentIds': self.studentIds(),
				}
			)
		return self

	def setContestId(self, contestId):
		self._contestId = contestId
		self._save()
		return self

	def setStudentNames(self, names):
		if self.launched():
			raise Exception("Student information is fixed after an instance is launched.")
		
		for index in range(len(names)):
			if index < len(names) and index < len(self._students):
				self._students[index].setName(names[index])
			elif index < len(names):
				self._students.append(Student.create(names[index]))

		if len(names) < len(self._students):
			for student in self._students[len(names):]:
				student.delete()
			self._students = list(self._students[:len(names)])

		return self

	def launch(self):
		self._launched = True
		for student in self._students:
			student.generateCredentials()
		self._save()
		return self

	def instanceId(self):
		return self._instanceId

	def contestId(self):
		return self._contestid

	def students(self):
		return tuple(self._students)

	def studentIds(self):
		return tuple(student.studentId() for student in self._students) # So our _students can't be modified.

	def launched(self):
		return self._launched

	

