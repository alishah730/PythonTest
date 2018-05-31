import re
import sqlite3
val = re.split(r'[aeiou]]', 'abcdefghij')
print(val)

con = sqlite3.connect('py.db')

cursor = con.cursor()

sql1 = 'DROP TABLE IF EXISTS EMPLOYEE'
sql2 = '''
CREATE TABLE EMPLOYEE(
EMPID INT(6) NOT NULL,
NAME CHAR(20) NOT NULL,
AGE INT,
SEX CHAR(1),
INCOME FLOAT
)
'''

#cursor.execute(sql1)
#cursor.execute(sql2)
print('SQL executed')

print('connection closed')

rec = (123214, 'Frodo', 45, 'M', 784151541.00522)

sql = '''INSERT INTO EMPLOYEE VALUES(?,?,?,?,?)'''

try:
    cursor.execute(sql, rec)
    con.commit()
except Exception as e:
    print("Error msg:", str(e))
    con.rollback()

records = cursor.fetchone()
print(records)
#for record in records:
#    print(record)

con.close()
