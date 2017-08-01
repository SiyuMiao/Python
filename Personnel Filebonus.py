#Siyu Miao

#creat a dictionary.
dic = {}
#open the file.
for i in open("dict_scores.txt","r").read().strip().split():
    #split by ":", on the left side of the : is name, on the right side of the : is score.
    #start with the value of zero, then add the 1(means the right side of the : is score) the score.
    dic[i.split(":")[0]] = dic.get(i.split(":")[0],0)+int(i.split(":")[1])
#print the dictionary
print dic










#I don't know how to put them into a dictionary.
#But I got the names and the correct numbers in one line.


##print [("Abby:",\
##        sum([int(i.split(":")[1])\
##             for i in open("dict_scores.txt","r").read().strip().split()\
##             if i.split(":")[0]=="Abby"])),\
##       ("Ben:",\
##        sum([int(i.split(":")[1])\
##             for i in open("dict_scores.txt","r").read().strip().split()\
##             if i.split(":")[0]=="Ben"])),\
##       ("Carl:",\
##        sum([int(i.split(":")[1])\
##             for i in open("dict_scores.txt","r").read().strip().split()\
##             if i.split(":")[0]=="Carl"]))]
       
