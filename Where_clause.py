import sqlite3

# connect to our database
conn = sqlite3.connect('customer.db')
# create a cursor
c = conn.cursor()

# Query database using Where clause
# primary key in sqlite3 is rowid
c.execute("""SELECT * FROM customers WHERE last_name = 'Elder' and age>=12 """)
# like allow finding all col = last_name bat dau voi Br
c.execute("""SELECT * FROM customers WHERE last_name LIKE 'Br%' """)
# Like allow finding all col = email ket thuc voi codemy.com
c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")

# store all table in items
items = c.fetchall()

for item in items:
    print(item)

# commit command
conn.commit()
# close database
conn.close()
