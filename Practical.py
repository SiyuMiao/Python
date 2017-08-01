
#Siyu Miao
import re, urllib
def find_majors(page):
        web_page = urllib.urlopen(page)
        lines = web_page.read()
        web_page.close()
        #create a list named major_span, by inspect element on the website, tr is in the lines, span is in the tr, major is in the span
        # . in "<span>.+?</span>" means all the characters also equal to [\w\W], but . not include \n(a new line), [\w\W] include \n(a new line)
        major_span = [re.findall("<span>.+?</span>",tr)[0] for tr in re.findall("<tr>.+?</tr>",lines) if re.findall("<span>.+?</span>",tr)]

        majors = [item.replace("<span>","").replace("</span>"," ") for item in major_span]
        return majors

def search_major(name):
            name=name.lower()
            match=[major for major in majors if re.findall(name,major.lower())]
	
            return match

page = "http://www.iub.edu/academic/majors/all.shtml"
majors = find_majors(page)
print "Parsing:",page,"\n\nMajors at IU:"
for major in majors:
        print major



print "\n\nParsing:",page
name=raw_input("\nPlease input a word to search for:")
matches=search_major(name)
for match in matches:
        print match
