#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python
import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

conn = sqlite3.connect("test7.db")

#y = x.getvalue("pro")
y=14
cursor=conn.execute("select * from product where pid=?",(y,))
c=list(cursor)
print( "Content-type:text/html\r\n\r\n")

print( '<!DOCTYPE html>')
print("<html><head><title>SELLING PAGE</title><link type='text/css' rel='stylesheet' href='/css_proj.css'>")
print("<link rel='icon' type='image/jpeg' href='pr.jpeg'></head><body>") 

for row in c:
         print("ID: <a href='",'six.py',"'>",row[0],"</a><br>" )
         print("Name: <a href='",'six.py',"'>",row[1],"</a><br>" )
         print("Brand: <a href='",'six.py',"'>",row[2],"</a><br>" )
         print("Price: <a href='",'six.py',"'>",row[3],"</a><br>" )
         print("Description: <a href='",'six.py',"'>",row[4],"</a><br><br>" )

print("<form action = '../cgi-bin/six.py' method='post'>")
#print("confirm order: <input type='input' id='pr' placeholder='Add product to buying cart'>")
print("<input type='submit' value='Confirm'>")
#print("<p> Order Placed </p>")

print("</body>")
print("</html>")

conn.close()
