# creating tables
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932', database='db2')
cur = mydb.cursor()
s = "CREATE TABLE Book(bookId integer(4), title varchar(20), price float(5, 2))"
cur.execute(s)
