#!/Python/python

import cgi,cgitb,sqlite3


#Connecting to database.
conn = sqlite3.connect('ams.db')
cur=conn.cursor()


#Getting data from form(index.html)
form=cgi.FieldStorage()
#usertype=(form["usertype"].value).strip()
username=(form["username"].value).strip()
password=(form["password"].value).strip()

#Query for getting data from admin or staff or student table.
query="select id,password from {0}"
query=query.format('staff')
cur.execute(query)
data=cur.fetchall()

#sessions here.
'''  '''
print ("Content-type: text/html\r\n\r\n");
#If not logged in checks for validity of user.	
if (username,password) not in data:
    print('''
	
    <html>
    <head>
    <title>Login Status</title>
    
    </head>
    <body><h2>Login Failed</h2>
    </body>
    </html>
	''')
else:
	print('''
	
    <html>
    <head>
    <title>Login Status</title>
    </head>
    <body><h2>Login Successful</h2>
    </body>
    </html>
	''')
	