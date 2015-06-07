

class Contest(object):

    def __init__(self, contestid):
        self._id = contestid
        self._name = getQuality("name")
        self._length = getQuality("length")
        self._description = getQuality("description")
        self._problems = getQuality("problems")

    def getQuality(self, quality):
        with conn.cursor() as cur:
            cur.execute("SELECT %(qual)s FROM contests WHERE id=%(me)s;", {'qual':quality, 'me':self.contestId()})
            return cur.fetchone()[0]

	def contestId(self):
        return self._id

	def name(self):
        return self._name

	def length(self):
        return self._length

	def description(self):
        return self._description

	def problems(self):
        return self._problems
