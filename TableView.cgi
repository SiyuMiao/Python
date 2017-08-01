#! /usr/bin/env python

print 'Content-type: text/html\n'

import MySQLdb, cgi

string = "i211s15_siyumiao" 		#change this to yours
password = "my+sql=i211s15_siyumiao"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()


try:				#Always surround .execute with a try!
        SQL = "SELECT * FROM Employee; "
        cursor.execute(SQL)
        results = cursor.fetchall()
except Exception, e:		#Here we handle the error
        print '<p>Something went wrong with the SQL!</p>'
        print SQL
        print "\nError:", e
else:				#This runs if there was no error
        print "<html><head><title>HR Center</title></head><body>"
        print "<h1>Human Resources Center</h1>"
        print "<h2>Employees</h2>"
        print "<table border='1' width='100%'>"
        print "<tr><th>EmployeeID</th><th>Name</th><th>Birth</th><th>City</th></tr>"
        for row in results:
            print "<tr>"
            for entry in row:
                print "<td align='center'>",entry,"</td>"
            print "</tr>"
        print "</table>"
        print"</body></html>"
print"""
<html>
<body>
<form action="TableView.cgi" method="get">
	<input type="submit" value="Add An Employee"><br />
</form>
</body>
</html>
"""

try:				#Always surround .execute with a try!
        SQL = "SELECT * FROM Job; "
        cursor.execute(SQL)
        results = cursor.fetchall()
except Exception, e:		#Here we handle the error
        print '<p>Something went wrong with the SQL!</p>'
        print SQL
        print "\nError:", e
else:				#This runs if there was no error
        print "<html><head><title>HR Center</title></head><body>"
        print "<h2>Jobs</h2>"
        print "<table border='1' width='100%'>"
        print "<tr><th>JobID</th><th>Title</th><th>Salary</th><th>EmployeeID</th></tr>"
        for row in results:
            print "<tr>"
            for entry in row:
                print "<td align='center'>",entry,"</td>"
            print "</tr>"
        print "</table></body></html>"
print"""
<html>
<body>
<form action="TableView.cgi" method="get">
	<input type="submit" value="Add A Job"><br />
</form>
</body>
</html>
"""

