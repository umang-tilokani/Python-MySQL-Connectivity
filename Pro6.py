# fetch records from database using python code
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932', database='db2')
cur = mydb.cursor()
s = "SELECT * from book"
cur.execute(s)
result = cur.fetchall()
for rec in result:
    print(rec)
    