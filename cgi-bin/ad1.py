#!C:\Python\Python37-32\python.exe

import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

u = x.getvalue("usr")
p = x.getvalue("pwd")
p2 = x.getvalue("pwd2")
n = x.getvalue("cn")
pn = x.getvalue("phn")
e = x.getvalue("em")

print( "Content-type:text/html\r\n\r\n")

conn=sqlite3.connect("test7.db")
cursor = conn.execute("select aid from admin;")
for row in cursor:
	if(u == row[0]):
		print("Select unique username")
	else: 
		continue

if (p == p2):
	continue
else :
	print("password do not match")

conn.execute("insert into admin values(" + u + ",'" + p + "'," + pn + ",'" + e + "');")
conn.execute("insert into admin_login values(" + u +",'" + p +"');")


print("Success")  
conn.close()