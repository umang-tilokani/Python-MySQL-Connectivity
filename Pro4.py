# insert records into database using python code
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932', database='db2')
cur = mydb.cursor()
s = "INSERT INTO Book(bookId, title, price) VALUES(%s, %s, %s)"
b1 = (101, "Ruby Programming", 673)
cur.execute(s, b1)
mydb.commit()
