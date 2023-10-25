# insert multiple records into mysql databse table using python code
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932', database='db2')
cur = mydb.cursor()
s = "INSERT INTO Book(bookId, title, price) VALUES(%s, %s, %s)"
books = [(104, "PHP", 698), (105, "Web Designing", 458), (106, "HTML", 812)] # multiple tuples inside list
cur.executemany(s, books)
mydb.commit()
