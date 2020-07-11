#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python
import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

conn = sqlite3.connect('test7.db')

print( "Content-type:text/html\r\n\r\n")

print( '<!DOCTYPE html>')
print("<html><head><title>SELLING PAGE</title><link type='text/css' rel='stylesheet' href='/css_proj.css'>")
print("<link rel='icon' type='image/jpeg' href='pr.jpeg'></head><body>") 

print("<p> Order Placed </p>")

print("</body>")
print("</html>")

conn.close()