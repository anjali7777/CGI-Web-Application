#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python

import cgi, cgitb, sqlite3
conn=sqlite3.connect("test7.db")
x = cgi.FieldStorage()


print( "Content-type:text/html\r\n\r\n")
print( "<!DOCTYPE html>")
print("<html><body><p>Product Added</p>")  
print ('<h1><a href="/customer_home.html">go to login page</a></h1>')
#print("window.alert('registered')")
print("</body></html>") 