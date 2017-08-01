import xml.etree.ElementTree as ET

root = ET.parse(source = 'menu.xml')

LI = []
for food in root.findall('food'):
        li=[]
        li.append(food.find('name').text)
        li.append(food.find('calories').text)
        li.append(food.find('price').text)
        LI.append(li)
		
LI = sorted(LI, key=lambda x:x[0])

print LI
data =LI
avg = sum([float(i[1]) for i in data])/len(data)
totalprice = sum([float(i[2][1:]) for i in data])

order = open("html_table.html","w")
order.write("<html><body><table border = '1' >")
order.write("<tr  align='center'>")
for elem in ['Item','Calories','Price']:
	order.write("<td><strong> "+str(elem)+"</strong></td>")
order.write("</tr>")

for sublist in data:
    order.write("<tr>")
    for elem in sublist:
        order.write("<td>"+str(elem)+"</td>")
    order.write("</tr>")

order.write("<td><strong>Average Calorie Value:"+str(avg)+"</strong></td>")

order.write("<td><strong>Total Price:</strong></td>")
order.write("<td><strong>"+"$"+str(totalprice)+"</strong></td>")
##order.write("</tr>")
order.write("</table></body></html>")

order.close()
