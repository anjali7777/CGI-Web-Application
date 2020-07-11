#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python

import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

u = x.getvalue("usr")
p = x.getvalue("pwd")

conn=sqlite3.connect("login.db")

conn.execute("create table customer_login(cid integer, password varchar(20),primary key(cid, password));")

conn.execute("insert into customer_login values(" + u +",'" + p +"');")


print( "Content-type:text/html\r\n\r\n")
print("Success")
conn.close()
