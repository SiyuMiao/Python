#Siyu Miao 
#Give the name of every letter in a dictionary.
print "---"
dictionary = {"A":"And","B":"Boy","C":"Clover",\
              "D":"Dog","E":"Exist","F":"Family",\
              "G":"Ground","H":"Home","I":"Itch",\
              "J":"Jeep","K":"Kids","L":"Lands",\
              "M":"Memery","N":"Never","O":"Over",\
              "P":"Plan","Q":"Question","R":"Rest",\
              "S":"Super","T":"Time","U":"Union",\
              "V":"Victory","W":"Wonder","X":"Xanadu",\
              "Y":"Yellow","Z":"Zero"}
hide = raw_input("What word should I hide? ").upper()
#Use for loop make the option of hide, and print the hide message.
for letter in hide:
    new_string = dictionary[letter]
    print new_string,
#Print the message for letting the message more hidden.
print "\n---","\nNow, let's make it a little more", "'hidden'", "by reversing their order!"
print "\n---"
#Use a list to store the more hidden message.
hide = raw_input("What word should I hide? ").upper()
more_hidden = []
#Use for loop make the option of hide.
for letter in hide:
    string = dictionary[letter]
    more_hidden += [string]
#Use while loop and .pop print out the more hidden message.
message = ""
while more_hidden:
    message += more_hidden.pop(len(more_hidden)-1)
    message += " "
print message
print "---"
