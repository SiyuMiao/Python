#Siyu Miao
from tools import*
table_print(["Name", "Age"],[i.split() for i in open("people.txt", "r").readlines()])



#This one also works well.
#table_print (["Name","Age"],[line.strip().split() for line in open("people.txt","r")])
