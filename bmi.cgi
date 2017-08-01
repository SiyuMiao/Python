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

form = cgi.FieldStorage()
#make sure the user type the correct information
if "weight" not in form:
    output = "Can't convert to numbers"
elif "fheight" not in form:
    output = "Can't convert to numbers"
elif "iheight" not in form:
    output = "Can't convert to numbers"
elif not form["weight"].value.isdigit():
    output = "Can't convert to numbers"
elif not form["fheight"].value.isdigit():
    output = "Can't convert to numbers"
elif not form["iheight"].value.isdigit():
    output = "Can't convert to numbers"

#get the information from user's input
else:
    weight = form["weight"].value
    height_feet = form["fheight"].value
    height_inches = form["iheight"].value
    BMI = "%.3f"%((float(weight)*703)/(((float(height_feet)*12)+float(height_inches))*((float(height_feet)*12)+float(height_inches))))
#output information
    output = "Your weight is: "+str("%.2f"%(float(form.getfirst("weight","None"))))+" lbs<br>"
    output += "<br>Your height is: "+str(form.getfirst("fheight","None"))+" feet "+str("%.2f"%(float(form.getfirst("iheight","None"))))+" inches<br>"
    output += "<br>Your BMI is: "+str(BMI)+"<br>"
#print out the information for the BMI in each level
    if float(BMI) < 15:
        output += "<br>BMI Category: Very severely underweight"
    elif float(BMI) < 16.0:
        output += "<br>BMI Category: Severely underweight"
    elif float(BMI) < 18.5:
        output += "<br>BMI Category: Underweight"
    elif float(BMI) < 25:
        output += "<br>BMI Category: Normal (healthy weight)"
    elif float(BMI) < 30:
        output += "<br>BMI Category: Overweight"
    elif float(BMI) < 35:
        output += "<br>BMI Category: Moderately obese"
    elif float(BMI) < 40:
        output += "<br>BMI Category: Severely obese"
    elif float(BMI) >= 40:
        output += "<br>BMI Category: Very severely obese"

print html.format(content=output)

#Reference:
#http://stackoverflow.com/questions/2075128/python-print-all-floats-to-2-decimal-places-in-output
