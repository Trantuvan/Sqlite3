import sqlite3
from employee_class import Employee

# database start fresh everytime from memory
conn = sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE employees(
            first text,
            last text,
            pay integer
            )""")

def insert_emp(emp):
    # with conn: contact manager do not need using commit and close
    with conn:
        c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",
            {'first':emp.first, 'last': emp.last, 'pay':emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""",
            {'first': emp.first,'last': emp.last,'pay': pay}) #dict "first" + "last" thi lay cua class emp.last or first but 'pay': pay to update

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
            {'first':emp.first,'last':emp.last})


emp_1 = Employee('Jane','Doe',90000)
emp_2 = Employee('John','Doe',10000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2,95000)
remove_emp(emp_1)

# muon display thong tin trong databse lan nua phai su dung query --> fetch
emps = get_emps_by_name('Doe')
print(emps)


conn.close()


# c.execute("INSERT INTO employees VALUES (?,?,?)",(emp_1.first, emp_1.last, emp_1.pay))

# c.execute("""INSERT INTO employees VALUES (:first,:last,:pay)""",
#     {'first':emp_2.first, 'last':emp_2.last, 'pay': emp_2.pay})
# conn.commit()

# c.execute("SELECT rowid, * FROM employees WHERE last = ? ", ('Shafer',))

# print(c.fetchall())

# c.execute("SELECT rowid, * FROM employees WHERE last =:last ", {'last':'Doe'})

# print(c.fetchall())

# conn.commit()
# conn.close()
