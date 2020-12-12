import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')
# create a cursor
c = conn.cursor()


# delete records
c.execute("""DELETE FROM customers WHERE first_name = 'Van'""")

# commit command
conn.commit()


# Query the database
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()
for item in items:
    print(item)

# close database
conn.close()
