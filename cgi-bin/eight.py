#!C:\Python\Python37-32\python.exe

import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

conn = sqlite3.connect("test8.db")

pr = x.getvalue("pro1")

conn.execute("delete from product where pid =" + pr +";")


print( "Content-type:text/html\r\n\r\n")
conn.close()
