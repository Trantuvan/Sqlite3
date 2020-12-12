import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')
# create cursor
c = conn.cursor()

# Query the limit database
# Limit must be at the end of the expression
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 5")

# store table in items
items = c.fetchall()

for item in items:
    print(item)

# commit command
conn.commit()
# close database
conn.close()
