# insert one record and return ID
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932', database='db2')
cur = mydb.cursor()
sql = "INSERT INTO Book(bookId, title, price) VALUES(%s, %s, %s)"
val = (104, "PHP", 708)
cur.execute(sql, val)
mydb.commit()
print("One Record Inserted!!, ID: ", cur.lastrowid)
