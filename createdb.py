import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(dbname="optimize")

conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
c = conn.cursor(cursor_factory=RealDictCursor)


c.execute('''DROP TABLE IF EXISTS users;''')


c.execute('''CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	firstname TEXT,
	lastname TEXT,
	email TEXT,
	phone TEXT,
	username TEXT,
	password TEXT
	);
''')

c.execute('''INSERT INTO users(firstname, lastname, email, phone, username, password) VALUES('david', 'caulfield', '@gmail', '5555555', 'david', 'password');''')



conn.commit()
conn.close()

