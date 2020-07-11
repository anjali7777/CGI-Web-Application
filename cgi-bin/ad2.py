#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python
import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

conn = sqlite3.connect('test7.db')

#u1 = x.getvalue("usr2")
#p1 = x.getvalue("pwd2")

print("Content-type:text/html\r\n\r\n")
print("<html><head><title>BUYING PAGE</title><link type='text/css' rel='stylesheet' href='/css_proj.css'>")
print("<link rel='icon' type='image/jpeg' href='pr.jpeg'></head><body>")

#cursor = conn.execute("select * from admin_login")

#for row in cursor:
	#if( u1 == row[0] && p1 ==row[1]):
		
		#cursor = conn.execute("select * from product")
		#for row in cursor:
			#print("<p>" + row + "</p> <br>")
        #print("<a href='adhome.html'>Go to home</a>")
		#print("</body>")
		#print("</html>")
	#else:
print("<h3><a href='/adhome.html'>Go to home</a></h3>")
print("</body>")
print("</html>")
		




conn.close()
