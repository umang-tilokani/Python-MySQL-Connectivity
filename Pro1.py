import mysql. connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932')
print(mydb.connection_id)
