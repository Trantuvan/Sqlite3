import sqlite3

# chi tao duoc 1 table thoi neu chay nhieu table cung ten loi

# connect a database
conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

many_customers = [
                ('Wes','Brown',23,'WesBrown@codemy'),
                ('Steph','Kuwed',33,'StephKuwed@gmail.com'),
                ('Van','Tran',24,'Trantuvan.kan@gmail.com'),
                ]


# insert one record into table
c.execute("INSERT INTO customers VALUES ('John','Elder',45,'John@codemy.com')")
c.execute("INSERT INTO customers VALUES ('John','Elder',12,'John@codemy.com')")
c.execute("""INSERT INTO customers VALUES ('Sue','Brown', 30,'SueBrown@codemy.com')""")
# insert many_record into table
c.executemany("""INSERT INTO customers VALUES (?,?,?,?)""", many_customers) # ? is placeholder in SQL


print('Command executed successfully!')
# commit our command
conn.commit()

# close our command
conn.close()
