import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')
# create a cursor
c = conn.cursor()

# Query the Database - AND/OR
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3")

# store table in items
items = c.fetchall()

for item in items:
    print(item)

# commit command
conn.commit()
# close database
conn.close()
