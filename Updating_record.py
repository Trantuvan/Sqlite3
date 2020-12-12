import sqlite3

# connect to our database
conn = sqlite3.connect('customer.db')
# create sursor
c = conn.cursor()

# Update records
c.execute("""UPDATE customers SET first_name = 'Bob'
                WHERE rowid = 1
    """)

c.execute("""UPDATE customers SET first_name = 'Marty'
                WHERE rowid = 4
    """)

# commit command to saving the command
conn.commit()

# Query the database
c.execute("SELECT rowid, * FROM customers")


items = c.fetchall()
for item in items:
    print(item)

# close database
conn.close()
