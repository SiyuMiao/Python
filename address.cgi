#! /usr/bin/env python
#Siyu Miao

import cgi
print 'Content-type: text/html\n'

html = """
<html>
    <head><title>Body Mass Index Calculator</title></head>
    <body>
        <p>{content}</p>
    </body>
</html>
"""
new_fname = ""
new_add1 = ""
new_add2 = ""
new_city = ""
new_state = ""
new_zip = ""
form = cgi.FieldStorage()
#make sure that user fills all the text boxes
if "fname" not in form:
    output = "Please fill in all the text boxes."
elif "add1" not in form:
    output = "Please fill in all the text boxes."
elif "add2" not in form:
    output = "Please fill in all the text boxes."
elif "city" not in form:
    output = "Please fill in all the text boxes."
elif "state" not in form:
    output = "Please fill in all the text boxes."
elif "zip" not in form:
    output = "Please fill in all the text boxes."
#get the informations from user's input
else:
    new_fname = form["fname"].value
    new_add1 = form["add1"].value
    new_add2 = form.getfirst("add2","")
    new_city = form["city"].value
    new_state = form["state"].value
    new_zip = form["zip"].value
#format the output
    output = "Name: "+str(new_fname)+"<br>"
    output += "Address: "
    output += "<br>"+str(new_add1)+str(new_add2)
    output += "<br>"+str(new_city)+", "+str(new_state)+", "+str(new_zip)

print html.format(content=output)

#bonus
create_file = open("address.txt", "a")
create_file.write("\n" + str(new_fname)+", "+str(new_add1)+", "\+str(new_add2)+", "+str(new_city)+", "+str(new_state)+", "+str(new_zip))
create_file.close()
