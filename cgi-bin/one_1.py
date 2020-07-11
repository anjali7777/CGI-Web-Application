#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python

import cgi, cgitb, sqlite3
conn=sqlite3.connect("test7.db")
x = cgi.FieldStorage()

u = x.getvalue("usr")
p = x.getvalue("pwd")
p2 = x.getvalue("pwd2")
n = x.getvalue("cn")
a = x.getvalue("adr")
pn = x.getvalue("phn")
e = x.getvalue("em")
y=1
z=1
i=0


cursor = conn.execute("select cid from customer;")
c1=list(cursor)
n=len(c1)
#for row in (0,n,1):
if u in c1:
		print("Select unique username")

		

	
data=[u,n,a,pn,e,z+1,y+1]
conn.execute("insert into customer values(?,?,?,?,?,?,?)",data)
#conn.execute("insert into customer_login values(" + u +",'" + p +"');")


print( "Content-type:text/html\r\n\r\n")
print( "<!DOCTYPE html>")
print("<html><body>")  
print("<p>'registered'</p>")
print ('<h1><a href="/login 1.html">go to login page</a></h1>')

print("</body></html>") 
#conn.close()
