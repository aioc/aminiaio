# Teacher model

class Teacher(object):

	@classmethod
	def login(cls, username, password):
		''' Returns a Teacher instance if the credentials are valid, or None otherwise. '''
		raise NotImplemented

	def save(self):
		raise NotImplemented

	def username(self):
		raise NotImplemented

	# username
	# contest instances and manipulation


