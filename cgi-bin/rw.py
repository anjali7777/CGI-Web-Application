#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python
import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

conn = sqlite3.connect("test7.db")

cursor = conn.execute("select * from product order by review desc ;")
print("Content-type:text/html\r\n\r\n") 
print("<html><head><title>BUYING PAGE</title><link type='text/css' rel='stylesheet' href='/css_proj.css'>")
print("<link rel='icon' type='image/jpeg' href='pr.jpeg'></head><body>")
	#cursor = conn.execute("select * from product where pid =? ",(y,))
for row in cursor:
	print("<a href='",'bu.html',"'>",row,"</a><br>" )
#print("<form action = 'bu.html' method ='post'>")
#print("<input type = 'submit' value='go to payment page'>")
#print("</form>")
print("</body>")
print("</html>")
