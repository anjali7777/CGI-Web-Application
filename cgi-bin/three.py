#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python
import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

conn = sqlite3.connect("test7.db")


cursor = conn.execute("select * from product")
print( "Content-type:text/html\r\n\r\n")

print("<html>")
print("<head>")
print("<title> Buying page </title>")
print("</head>")
print("<body>")
for row in cursor:
	print("<p>" , row , "</p> <br>")
print("<form action = '../cgi-bin/sr.py' method='post'>")
print("<input type='input' id='search' placeholder='Add product to buying cart'>")
print("<input type='submit' value='Go to buying kart'><br>")

print("<form action = '../cgi-bin/pl.py' method='post'>")
print("<input type='input' id='plt' placeholder='price less than'>")
print("<input type='submit' value='Go to buying kart'><br>")

print("<form action = '../cgi-bin/four.py' method='post'>")
print("<input type='input' id='pmt' placeholder='price more than'>")
print("<input type='submit' value='Go to buying kart'><br>")

#print("<input type='checkbox' id='rating' value = 'off'><br>")

print("<form action = '../cgi-bin/four.py' method='post'>")
print("enter product id to add to cart: <input type='input' id='pro' placeholder='Add product to buying cart'>")
print("<input type='submit' value='Go to buying kart'>")
print("</form>")
print("</body>")
print("</html>")

conn.close()
