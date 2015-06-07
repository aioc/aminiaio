#need to define 
#and import psycopg2
class Problem(object):

    def __init__(self, name):
        self._name = name
        self._title = self.getQuality("title")
        self._hardness = self.getQuality("hardness")
        self._flavourText = self.getQuality("description")
        self._hints = self.getQuality("hints")
        self._solution = self.getQuality("solution")

    def getQuality(self, quality):
        with conn.cursor() as cur:
            cur.execute("SELECT %(qual)s FROM problems WHERE name=%(me)s;", {'qual':quality, 'me':self.problemName()})
            return cur.fetchone()[0]

	def flavourText(self):
        return self._flavourText

	def hints(self):
        return self._hints
        
	def solution(self):
        return self._solution

    def hardness(self):
        return self._hardness
    
    def problemName(self):
        return self._name

    def problemTitle(self):
        return self._title

	def problemName(self):
        return self._name

