# fetch-one record from database using python code
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932', database='db2')
cur = mydb.cursor()
cur.execute("SELECT * from Book")
res = cur.fetchone()
print(res)
