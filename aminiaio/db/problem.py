from . import conn

class Problem(object):

	def __init__(self, problemId, name, hardness, description, hints, solution):
		self._problemId = problemId
		self._name = name
		self._hardness = hardness
		self._description = description
		self._hints = hints
		self._solution = solution

	@classmethod
	def load(cls, problemId):
		with conn.cursor() as cur:
			cur.execute(
				'SELECT name, hardness, description, hints, solution FROM problems WHERE problem_id=%s;',
				(problemId,))
			result = cur.fetchone()
			if result is None:
				return None
			name, hardness, description, hints, solution = result
			return cls(problemId, name, hardness, description, hints, solution)

	@classmethod
	def create(cls, name, hardness, description, hints=None, solution=None):
		with conn.cursor() as cur:
			cur.execute('''
				INSERT INTO problems (name, hardness, description, hints, solution)
				VALUES (%(name)s, %(hardness)s, %(description)s, %(hints)s, %(solution)s)
				RETURNING problem_id;
			''', {
				'name': name,
				'hardness': hardness,
				'description': description,
				'hints': hints,
				'solution': solution,
			})
			problemId, = cur.fetchone()
			return cls.load(problemId)


	def problemId(self):
		return self._problemId

	def name(self):
		return self._name

	def hardness(self):
		return self._hardness

	def description(self):
		return self._description

	def hints(self):
		return self._hints
		
	def solution(self):
		return self._solution


