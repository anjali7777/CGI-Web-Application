#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python
import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

conn = sqlite3.connect("test7.db")

cursor = conn.execute("select * from product where price >" + c + ";")

print("<html>")
	print("<head>")
	print("<title> Buying kart </title>")
	print("</head>")
	print("<body>")
	cursor = conn.execute("select * from product where pid =? ",(y,))
	for row in cursor:
		print("<p>" + row +"</p>")
	print("<form action = 'five.py' method ='post'>")
	print("<input type = 'submit' value='go to payment page'>")
	print("</form>")
	print("</body>")
	print("</html>")