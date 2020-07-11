import sqlite3
import cgi,cgitb
conn=sqlite3.connect('lab7q3.db')
cursor=conn.execute('create table validate(id int not null,password int not null);')
conn.execute('insert into validate values(132221,23123)')
conn.execute('insert into validate values(1321,23923)')
print("login sucessful")
conn.commit()
cursor=conn.execute('select id from validate')
cursor2=conn.execute('select password from validate')
f=cgi.FieldStorage()
user=f.getvalue('name')
pwd=f.getvalue('name2')
if user in cursor:
    print("login unsucessful")
if pwd in corsor2:
    print("login unsucessful")
else:
    print("login sucessful")

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello %s %s</h2>" % (user, pwd))
print ("</body>")
print ("</html>")