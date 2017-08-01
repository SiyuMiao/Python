###Name: Siyu Miao
import urllib, re
#create function of getStockData(company)
def getStockData(company):
    #return these values.
    lastTrade = ""
    change = ""
    date = ""
    open = ""
    previousClose = ""
    flag = ""
    #I use the website without the company name,
    #so I want to select the name one by one into the function,
    #then I use the website plus the company name and return the values.
    web_page = urllib.urlopen(url+company)
    lines = web_page.read()
    web_page.close()

#From here, I will use "." which means all the characters also equal to [\w\W]
    #Get the value of the last trade
    line = re.findall('<span id="yfs_l84_.*?">.+?</span>',lines)[0]
    lastTrade = line.replace(">","<").split("<")[2]
    #Get the value of the change
    line = re.findall('<span id="yfs_c63_.*?">.+?</span>',lines)[0]
    change = line.replace(">","<").split("<")[4].strip()
    #Get the value of the date
    line = re.findall('<span id="yfs_t53_.*?">.+?</span>',lines)[0]
    date = line.replace(">","<").split("<")[2].split(",",3)[0]+", 2015"
    #Get the value of the open
    line = re.findall('Open:</th><td class="yfnc_tabledata1">.+?</td>',lines)[0]
    open = line.replace(">","<").split("<")[4]
    #Get the value of the previousClose
    line = re.findall('Prev Close:</th><td class="yfnc_tabledata1">.+?</td>',lines)[0]
    previousClose = line.replace(">","<").split("<")[4]

    if float(lastTrade) <= float(previousClose):
        flag = "-"

    return lastTrade, change, date, open, previousClose, flag

#create the function of find stock
def find_stock(page):
    web_page = urllib.urlopen(page)
    lines = web_page.read()
    web_page.close()
    
    #Find all  companies name on page
    companies = [item.replace(">","<").split("<")[6].strip() for item in re.findall('<div class="companyName">.+?</div>',lines)]

    return companies

#create the function of information
def information(company):
    #Get the return values in the function of getStockData(company)
    #print the information of the selected company
    lastTrade, change, date, open, previousClose, flag = getStockData(company)


    # %s is a easy way to print out the statement whithout "+" or "," one by one in the "()"
    print "\nThe last trade for %s was $%s and the change was %s$%s on %s. The open was $%s and the previous close was $%s."\
          %(company, lastTrade, flag, change, date, open, previousClose)



#main
#Basic website
url = "http://finance.yahoo.com/q?s="
#Select 10 companies
coms = ["GOOG", "GE", "KO", "DIS", "PG", "BA", "WFC", "HPQ", "AXP", "MMM"]
for com in coms:
    information(com)


#Bonus
print "\n","*"*30
print "BONUS:"
print "*"*30
#Basic website
page = "http://www.fool.com/the-25-best-companies-in-america/index.aspx"
for com in find_stock(page):
    information(com)

















