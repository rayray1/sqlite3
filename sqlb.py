# INSERT Command with Error Handler


# import the sqlite3 library
import sqlite3


# create the connection object
conn = sqlite3.connect("new.db")


# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
	# insert data
	cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 5000000)")
	cursor.execute("INSERT INTO population VALUES('San Fransisco', 'CA', 800000)")


	# commit the changes
	conn.commit()

except sqlite3.OperationalError:
	print "OOps! Something went wrong. Try Again..."


# close the database connection
conn.close()