import sqlite3

# create the sql in memory but when u stop the program can't use it
# conn = sqlite3.connet(':memory:')

# connect to the database in this directory
conn = sqlite3.connect('customer.db')

# create the cursor the interact with database
c = conn.cursor()

# create the table
c.execute("""CREATE TABLE customers(
        first_name text,
        last_name  text,
        age integer,
        email     text
)""")


# 5 types of datatypes in sqlite
# NULL : boolean
# INTEGER : 1,9,125
# REAL : 19.9, 9.0
# TEXT : 'van'
# BLOB : img, mp3,

# commit our command
conn.commit()

# close our connection
conn.close()
