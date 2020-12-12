import sqlite3

# connect to our database
conn = sqlite3.connect('customer.db')

# create the cursor
c = conn.cursor()

# Query the database to display data
# primary key in sqlite3 is rowid
c.execute("""SELECT rowid,* FROM customers""")
# Fetch data the see in console

# print all table
items = c.fetchall()
for item in items:
    print(item)

# print one row
# print(c.fetchone())

# print many row can specified
# print(c.fetchmany(5))


print('Command executed successfully...')
# commit our command
conn.commit()
# close our connection
conn.close()
