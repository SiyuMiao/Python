#Siyu Miao
import re, urllib
def find_majors(page):
    web_page = urllib.urlopen(page)
    lines = web_page.read()
    web_page.close()

    major_span = [re.findall("<span>.+?</span>",tr)[0] for tr in re.findall("<tr>.+?</tr>",lines) if re.findall("<span>.+?</span>",tr)]

    majors = [item.replace("<span>","").replace("</span>"," ") for item in major_span]
    return majors



page = "http://www.iub.edu/academic/majors/all.shtml"
majors = find_majors(page)
print "Parsing:",page,"\n\nMajors at IU:"
for major in majors:
    print major

print "\nParsing:",page
name=raw_input("\nPlease input a word to search for:")
matches=search_major(name)
for match in matches:
	print match
