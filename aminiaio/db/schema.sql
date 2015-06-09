CREATE TABLE problems (
	problem_id  SERIAL  PRIMARY KEY,
	name        TEXT    NOT NULL UNIQUE,
	hardness    TEXT    NOT NULL,
	description TEXT    NOT NULL,
	hints       TEXT    NULL,
	solution    TEXT    NULL
);

CREATE TABLE students (
	student_id  SERIAL  PRIMARY KEY,
	name        TEXT    NOT NULL,
	username    TEXT    NULL UNIQUE,
	password    TEXT    NULL
);

CREATE TABLE contests (
	contest_id  SERIAL  PRIMARY KEY,
	name        TEXT    NOT NULL,
	length      INT     NOT NULL,
	description TEXT    NOT NULL,
	problems    INT[]   NOT NULL
);

CREATE TABLE instances (
	instance_id SERIAL  PRIMARY KEY,
	contest_id  INT     NOT NULL REFERENCES contests(contest_id),
	students    INT[]   NOT NULL, -- REFERENCES students(student_id), but can't make constraint explicit
	launched    BOOLEAN NOT NULL
);

CREATE TABLE teachers (
	teacher_id  SERIAL  PRIMARY KEY,
	username    TEXT    NOT NULL UNIQUE,
	passhash    TEXT    NOT NULL,
	instances   INT[]   NOT NULL, -- REFERENCES instances(instance_id), but can't make constraint explicit
	UNIQUE(username)
);
