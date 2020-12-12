import sqlite3

# connect to our database
conn = sqlite3.connect('customer.db')
# create a cursor
c = conn.cursor()

# Query the database - Order by
c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

# store database in items
items = c.fetchall()

for item in items:
    print(item)

# commit command
conn.commit()
# close database
conn.close()
