import psycopg2
from psycopg2.extras import RealDictCursor
import wrapper

conn = psycopg2.connect(dbname="optimize")

conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
c = conn.cursor(cursor_factory=RealDictCursor)


class User:

	@classmethod
	def login(cls, uname, pword):
		c.execute('''SELECT * FROM users;''')
		result = c.fetchone()
		print(result)
		print(uname, pword)
		c.execute("SELECT * FROM users WHERE username=(%s) AND password=(%s);", (uname, pword))
		result = c.fetchone()
		print(result)
		if result:
			return True
		else:
			return False

	@classmethod
	def check_register(cls, username):
		c.execute('''SELECT * FROM users WHERE username=%s;''', (username,))
		result = c.fetchone()
		if result:
			return True
		else:
			return False

	@classmethod
	def register(cls, fname, lname, email, phone, username, password):
		c.execute('''INSERT INTO 
			users(firstname,lastname,email,phone,username,password) 
			VALUES
			(%s,%s,%s,%s,%s,%s);
			''', 
			(fname, lname, email, phone, username, password)
		)

	@classmethod
	def register(cls, **kwargs):
		c.execute('''INSERT INTO 
			users(firstname,lastname,email,phone,username,password) 
			VALUES
			(%(fname)s, %(lname)s, %(email)s, %(phone)s, %(user)s, %(pass)s);
			''', 
			kwargs
		)
		









