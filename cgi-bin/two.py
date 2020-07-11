#!C:/Users/KIIT/AppData/Local/Programs/Python/Python36/python

import cgi, cgitb, sqlite3

x = cgi.FieldStorage()

conn = sqlite3.connect("test7.db")

u1 = x.getvalue("usr1")
p1 = x.getvalue("pwd1")
i=0
j=0
#import os,webbrowser
#u2=u1+','
#os.startfile('customer_home.html')
cursor1 = conn.execute("select cid from customer_login")
c1=list(cursor1)
#print(cursor1)
#print(c1)
#print(u1,p1)
print ('Content-type: text/html\r\n\r\n')
print( '<!DOCTYPE html>')
print ('<html ')
print( '  <head> ')
print (' </head>')
print ('<body>')

#for row in cursor1: 
if u1 in cursor1:

    print (' <h1><a href="/customer_home.html">go to customer page</a></h1>')
    print (' <h1><a href="/login 1.html">Go back</a></h1>')

else:
        #print("Invalid")
    print (' <h1><a href="/customer_home.html">go to customer page</a></h1>')
    

print( '</body>')
print( '</html>')

#for row in cursor:
	#if(u1 == row[i]):
		#break
	#else:
		#i++ 
		#continue

#cursor = conn.execute("select password from customer_login")

#for row in cursor:
	#if(p1 == row[j]):
		#break
	#else:
		#j++ 
		#continue





