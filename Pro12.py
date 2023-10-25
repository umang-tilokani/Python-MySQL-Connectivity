# select with a filter
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932', database='db2')
cur = mydb.cursor()
cur.execute("SELECT * FROM Book WHERE bookId='103'")
res = cur.fetchall()
for x in res:
    print(x)
