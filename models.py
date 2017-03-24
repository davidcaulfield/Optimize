import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(dbname="optimize")

conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
c = conn.cursor(cursor_factory=RealDictCursor)


class User():

	@classmethod
	def login(cls, uname, pword):
		c.execute('''SELECT * FROM users;''')
		result = c.fetchone()
		print(result)
		print(uname, pword)
		c.execute("SELECT * FROM users WHERE username='{0}' AND password='{1}';".format(uname, pword))
		result = c.fetchone()
		print(result)
		if result:
			return True
		else:
			return False

	@classmethod
	def check_register(cls, user):
		c.execute('''SELECT * FROM users WHERE username=?;''')
		result = c.fetchone()
		if result:
			return True
		else:
			return False

	@classmethod
	def register(cls, fname, lname, email, phone, users, password):
		c.execute('''INSERT INTO users(firstname, lastname, email, phone, username, password) VALUES(?, ?, ?, ?, ?, ?);''', (fname, lname, email, phone, users, password))
		c.commit()









