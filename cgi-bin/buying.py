#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python

import cgi, cgitb, sqlite3
conn=sqlite3.connect("test7.db")
form = cgi.FieldStorage()

 
  
print("Content-type:text/html\r\n\r\n") 
print( '<!DOCTYPE html>')
print("<html><head><title>SELLING PAGE</title><link type='text/css' rel='stylesheet' href='/css_proj.css'>")
print("<link rel='icon' type='image/jpeg' href='pr.jpeg'></head><body><table>") 

# Using the inbuilt methods 
  

search = form.getvalue("s1")

#print(search)

c1=conn.execute("select * from product where pname = ? ",(search,))
c=list(c1)
#d=open("bu.html","a")
#.write("""<head><title>SELLING PAGE</title></head><body><table>ytrsgeegzsfd</table></body></html>""")  
for row in c:    
    print("<tr><td>Product Detail: <a href='",'/bu.html',"'>",row,"</a></td></tr>")   

print("</table></body></html>")
  
