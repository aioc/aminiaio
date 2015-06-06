CREATE TABLE problems (
    name        VARCHAR(40),
    title       INT,
    hardness    TEXT,
    description TEXT,
    hints       TEXT
    solution    TEXT,
    UNIQUE(name));

CREATE TABLE students (
    name        VARCHAR(80),
    username    VARCHAR(90),
    password    VARCHAR(15),
    UNIQUE(username));

CREATE TABLE contests (
    id          INT,
    name        VARCHAR(40),
    length      INT,
    description TEXT,
    problems    VARCHAR(40)[],
    UNIQUE(id));

CREATE TABLE instances (
    id          INT,
    contestid   INT,
    students    VARCHAR(90)[],
    launched    BOOLEAN,
    UNIQUE(id));

CREATE TABLE teachers (
    username    VARCHAR(40),
    passhash    VARCHAR(255),
    instances   INT[],
    UNIQUE(username));
