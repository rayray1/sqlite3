# executemany() method

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# insert multiple records using a tuple
	cities = [
			('Boston', 'MA', 700000),
			('Chicago', 'IL', 500000),
			('Houston', 'TX', 450000),
			('Phoenix', 'AZ', 300000)
			]

	# insert data into table
	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)