Databases
- for these examples I'm using SQL Lite Browser
- a database is a group of data organised into rows and columns
- SQL:
  - Structured Query Language
- relational databases are scalable

What you can do with databases:
  - CRUD
  - Create
  - Read
  - Update
  - Delete

- web applications use databases in the backend to store data
- databases will have a Database Administrator who is in charge of the database and the data

Common Database Systems:
  - Oracle
  - MySQL
  - SQLServer
  - Posgres

  SQLlite:
    - it is an embeded database

  SQL Commands:
    - Create a table = CREATE TABLE <table name> (<column name> <column attribute, text or numbers etc>, <column name> <column attribute, text or numbers etc>)
    - Insert data = INSERT INTO <table name> (<column name>, <column name>) VALUES ("<column 1 value>", "<column 2 value>")
    - Update = UPDATE <table name> SET <column> = "<new value>" WHERE <column> = "<value>"
    - Delete = DELETE FROM <table name> WHERE <column> = "<value>"
    - Retrieve = SELECT *(* means all) FROM <table name> ORDER BY <column to order the data according to> DESC (desc = descending order)

Relational Databases:
  - data model - the layout of how different tables within the database relate to each other and share information
  - relationships:
    - 1 to 1
    - 1 to many
    - many to many
  - you should never have the same string data in more than one table within a database
  - using the relational database method means that updating data is simpler and displaying data is faster due to the lesser size of a number primary key compared with the string text

Database Normalisation:
  - this is the idea of creating a database where string data isn't repeated

Keys:
  - primary key - the ID for a row, should be a number that is unique
  - logical key - the string that other tables see associated to the primary key
  - foreign key - the primary key that appears in another table
  - a logical key should never be a primary key, this is because logical keys can change

Join operation:
  - this joins tables and using the ON function you can integrate the foreign keys to the primary keys of their main table

Many to many relationship:
  - you can't have a many to many relationship within a table
  - you need to create a connection table which only has foreign keys in it which when the two foreign keys are paired together they act as the primary key for that row on the table

books <-----> authors

              Connection table
books <------> authors
               books  <-----> authors
Tracks Database:
  - Commands:
      CREATE TABLE "Artist" (
      "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
      "name" TEXT)

      CREATE TABLE "Album" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        artist_id INTEGER,
        "title" TEXT)

      CREATE TABLE "Genre" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        "name" TEXT)

      CREATE TABLE "Track" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER,
        "title" TEXT, "count" INTEGER)

      CREATE TABLE "<name>" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        "<column>" TEXT)

    - SELECT statements:
    SELECT Album.title, Artist.name FROM Album JOIN Artist
    ON Album.artist_id = Artist.id

    SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id
    AND Album.artist_id = Artist.id

    Example:
    SELECT <table name>.<logical key column>, <table name>.<logical key column>, <table name>.<logical key column>
    FROM <primary table name> JOIN <other table> JOIN <other table> JOIN <other table>
    ON <primary table>.<foreign key column> = <other table>.<primary key column> AND <primary table>.<foreign key column> = <other table>.<primary key column> AND <primary table>.<foreign key column> = <other table>.<primary key column>

Many to Many database:
  CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
  ) ;

  CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
  ) ;

  CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
  role        INTEGER,
    PRIMARY KEY (user_id, course_id)
  ) ;

  INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
  INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
  INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

  INSERT INTO Course (title) VALUES ('Python');
  INSERT INTO Course (title) VALUES ('SQL');
  INSERT INTO Course (title) VALUES ('PHP');

  INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
  INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
  INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

  INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
  INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

  INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
  INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);

  SELECT User.name, Member.role, Course.title
  FROM User JOIN Member JOIN Course
  ON Member.user_id = User.id AND Member.course_id = Course.id
  ORDER BY Course.title, Member.role DESC, User.name
