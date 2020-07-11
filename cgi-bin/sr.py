#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python
import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

conn = sqlite3.connect("test7.db")

a = x.getvalue("search")

print( "Content-type:text/html\r\n\r\n")
print(a)
cursor = conn.execute("select * from product")

print("<html><head><title>SELLING PAGE</title><link type='text/css' rel='stylesheet' href='/css_proj.css'>")
print("<link rel='icon' type='image/jpeg' href='pr.jpeg'></head><body>")
print("<h3>All Products</h3>")

                #cursor = conn.execute("select * from product where pid =? ",(y,))
for row in cursor:
         print("Product Details: <a href='",'/bu.html',"'>",row,"</a>" )
         #print("Name: <a href='",'/bu.html',"'>",row[1],"</a>" )
         print("Name: <a href='",'/bu.html',"'>",row[2],"</a>" )
         print("Name: <a href='",'/bu.html',"'>",row[3],"</a>" )
         print("Name: <a href='",'/bu.html',"'>",row[4],"</a>" )
#print("<form action = 'five.py' method ='post'>")
#print("enter product id: <input type='input' id='pmt' placeholder='price more than'>")
#print("<input type = 'submit' value='go to payment page'>")
print("</form>")
print("</body>")
print("</html>")
