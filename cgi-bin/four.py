#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python
import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

conn = sqlite3.connect("test7.db")

y = x.getvalue("pro")


print( "Content-type:text/html\r\n\r\n")

if x.getvalue("search"):
	a = x.getvalue("search")
	print("<html>")
	print("<head>")
	print("<title> Product </title>")
	print("</head>")
	print("<body>")
    print("<form action = 'sr.py' method ='post' >")
	cursor = conn.execute("select * from product where pname like =?",(a,))
	for row in cursor:
		print("<p>" + row + "</p> <br>")
        
    
	print("<input type = 'submit' value='search'>")
	print("</form>")
	print("</form>")
	print("</body>")
	print("</html>")

elif x.getvalue("plt"):
	b = x.getvalue("plt")
	print("<html>")
	print("<head>")
	print("<title> Product </title>")
	print("</head>")
	print("<body>")
    print("<form action = 'pl.py' method ='post'>")
	print("<input type = 'submit' value='amount less'>")
	cursor = conn.execute("select * from product where price < " + b + ";")
	for row in cursor:
		print("<p>" + row + "</p> <br>")
	print("</form>")
	print("</body>")
	print("</html>")

elif x.getvalue("pmt"):
	c = x.getvalue("pmt")
	print("<html>")
	print("<head>")
	print("<title> Product </title>")
	print("</head>")
	print("<body>")
	cursor = conn.execute("select * from product where price >" + c + ";")
	for row in cursor:
		print("<p>" + row + "</p> <br>")
	print("</form>")
	print("</body>")
	print("</html>")

elif x.getvalue("rating"):
	print("<html>")
	print("<head>")
	print("<title> Product </title>")
	print("</head>")
	print("<body><fo")
	cursor = conn.execute("select * from product order by review desc ;")
	for row in cursor:
		print("<p>" + row + "</p> <br>")
	print("</form>")
	print("</body>")
	print("</html>")


else:
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

conn.close()




