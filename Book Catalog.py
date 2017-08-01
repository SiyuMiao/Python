###Name: Siyu Miao
import xml.etree.ElementTree as ET

root = ET.parse(source = "books.xml")
print "Individual HW 2: Book Catalog\nPart a"
print "-"*40
#create a function and print out the title, author, price of each book.
def book_info(id):
    #find the title author and price of the book
    print "The book with id =",id,\
          "\n".join(["\nTitle: "+book.find("title").text+\
                     "\nAuthor: "+book.find("author").text+\
                     "\nPrice: "+book.find("price").text for book in root.findall("book") if book.items()[0][1] == id])

#main
#find out the id for each book
for id in [book.items()[0][1] for book in root.findall("book")]:
    book_info(id)
    print "-"*30


print "\nPart b"
print "-"*75
#find out the genre is computer and sum of the price of the books
print "The total cost of buying all the books in the 'Computer' genre is",\
      sum([float(book.find("price").text) for book in root.findall("book") if book.find("genre").text == "Computer"])
print "-"*75



print "\nPart c"
print "-"*40
#create a dictionary
##dic = {}
#find out the type of the book, and count the times of the type appears
##for types in root.findall("book/genre"):
##    dic[types.text] = dic.get(types.text,0)+1
#print out the book that which one just appear one time
##print "The unique genres in the file are:\n",\
##      ",".join([types[0] for types in dic.items() if types[1]==1])



#genre[0] means the type of the book and genre[1] means how many times appear
#creat a dictionary in the list and collect the type and the times of the type appears
#collect the time equal to 1
print "The unique genres in the file are:\n",\
      ",".join([types[0] for types in\
                {elem:[i.text for i in root.findall("book/genre")].count(elem)\
                 for elem in [i.text for i in root.findall("book/genre")]}.items() if types[1]==1])
print "-"*40


#REFERENCE
#https://www.python.org/dev/peps/pep-0274/
#http://stackoverflow.com/questions/1747817/python-create-a-dictionary-with-list-comprehension
