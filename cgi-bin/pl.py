#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python
import cgi, cgitb, sqlite3

x = cgi.FieldStorage()
#b=x.getvalue("n1")
#c=x.getvalue("n2")
b=int(10)
c=1000
conn = sqlite3.connect("test7.db")

cursor = conn.execute("select * from product where price < ?",(c,))

print("Content-type:text/html\r\n\r\n") 
print( '<!DOCTYPE html>')
print("<html><head><title>SELLING PAGE</title><link type='text/css' rel='stylesheet' href='/css_proj.css'>")
print("<link rel='icon' type='image/jpeg' href='pr.jpeg'></head><body>")
	#cursor = conn.execute("select * from product where pid =? ",(y,))
for row in cursor:
	print( row,"<br>" )
print("<form action = 'five.py' method ='post'>")
print("<input type = 'submit' value='go to payment page'>")
print("</form>")
print("</body>")
print("</html>")
