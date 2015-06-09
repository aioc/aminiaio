from .db import Teacher

def login(username, password):
	return Teacher.login(username, password)

def create(username, password):
	assert usernameValid(username) and passwordValid(password)
	return Teacher.create(username, password)

def usernameDescription():
	return 'Usernames must have at least 5 characters, and can only contain letters, numbers, dashes, and underscores.'

def usernameValid(username):
	return len(username) > 4 and \
		all('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9' or c in '-_' for c in username)

def passwordDescription():
	return 'Passwords must have at least 5 characters.'

def passwordValid(password):
	return len(password) > 4