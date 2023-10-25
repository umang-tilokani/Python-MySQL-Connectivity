# selecting columns
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932', database='db2')
cur = mydb.cursor()
cur.execute("SELECT title, price from Book")
res = cur.fetchall()
for x in res:
    print(x)
    