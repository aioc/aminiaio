from . import conn

class Contest(object):

	def __init__(self, contestId, name, length, description, problems):
		self._contestId = contestId
		self._name = name
		self._length = length
		self._description = description
		self._problems = problems

	@classmethod
	def load(cls, contestId):
		with conn.cursor() as cur:
			cur.execute('SELECT name, length, description, problems FROM contests WHERE contest_id=%s;', (contestId,))
			result = cur.fetchone()
			if result is None:
				return None
			name, length, description, problems = result
			return cls(contestId, name, length, description, problems)

	@classmethod
	def create(cls, name, length, description, problems):
		with conn.cursor() as cur:
			cur.execute('''
				INSERT INTO contests (name, length, description, problems)
				VALUES (%(name)s, %(length)s, %(description)s, %(problems)s)
				RETURNING contest_id;
			''', {
				'name': name,
				'length': length,
				'description': description,
				'problems': problems,
			})
			contestId, = cur.fetchone()
			return cls.load(contestId)
	

	def contestId(self):
		return self._contestId

	def name(self):
		return self._name

	def length(self):
		return self._length

	def description(self):
		return self._description

	def problems(self):
		return self._problems
