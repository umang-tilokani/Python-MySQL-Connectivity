# delete records from mysql database using python code
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932', database='db2')
cur = mydb.cursor()
s = "DELETE FROM Book where title = 'PHP'"
cur.execute(s)
mydb.commit()
