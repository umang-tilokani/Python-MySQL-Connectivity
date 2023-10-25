# create database
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Um@ng1932')
cur = mydb.cursor()
cur.execute("CREATE DATABASE db2")
