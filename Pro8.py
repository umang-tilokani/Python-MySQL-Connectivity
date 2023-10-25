# update records using python code
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932', database='db2')
cur = mydb.cursor()
s = "UPDATE Book SET price = price + 10 where price > 200"
cur.execute(s)
mydb.commit()
