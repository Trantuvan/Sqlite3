import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')
# create a cursor
c = conn.cursor()

# Drop Table
c.execute("DROP TABLE customers")

# commit command
conn.commit()

# Query the table
c.execute("SELECT rowid, * FROM customers WHERE rowid = 3")
items = c.fetchall()
for item in items:
    print(item)

# commit command
conn.commit()
# close database
conn.close()
