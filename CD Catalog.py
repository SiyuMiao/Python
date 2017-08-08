###Name: Siyu Miao
import xml.etree.ElementTree as ET

root = ET.parse(source = "cd_catalog.xml")


#find out the numbers of total CD
print "The total number of CDs is",(len(root.findall("CD")))
#find out the price of each one and add them together
print "The total price of purchasing one of each is",(sum([float(price.text) for price in root.findall("CD/PRICE")]))
print "-"*60


print "Part b:"
#find out the minimum price of the CD
print "The minimum price of the CDs is",(min([float(price.text) for price in root.findall("CD/PRICE")]))
#find out the maximum price of the CD
print "The maximum price of the CDs is",(max([float(price.text) for price in root.findall("CD/PRICE")]))
#find out the average price of the CD
print "The average price of the CDs is",(sum([float(price.text) for price in root.findall("CD/PRICE")])/len(root.findall("CD")))
print "-"*60


print "Part c:"
#find out the CD that which one relased in the year 1990
print "The total number of CDs released in the year 1990 is",(len([year for year in root.findall("CD/YEAR") if year.text == "1990"]))
print "-"*60


print "Part d:"
#find out the CD that which one's artist comes from america
print "The names of all artists who are from America(USA):\n",",".join([cd.find("ARTIST").text for cd in root.findall("CD") if cd.find("COUNTRY").text == "USA"])
print "-"*60
