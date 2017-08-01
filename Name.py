#Siyu Miao
thefile = [line for line in open("name.txt","r").read().split()]
print "Current Suspects:\n"+"-"*17+"\n"+" ".join(sorted(thefile))

clue1 = [name for name in thefile if len(name)<=6]
print "\n*** Clue 1: The killer's name is no more than 6letters long. ***\n\nCurrent Suspects:\n"+"-"*17+"\n"+" ".join(sorted(clue1))+"\n"

clue2 = [name for name in clue1 if name[0] != "D" and name[-1] not in "AEIOU"]
print "\n*** Clue 2: The killer's name doesn't end in a vowel or start with 'D'. ***\n\nCurrent Suspects:\n"+"-"*17+"\n"+" ".join(sorted(clue2))+"\n"


clue3 = [name for name in clue2 if len([letter for letter in name if letter in "AEIU"])==2]
print "\n*** Clue 3: The killer's name has two vowels in it that are not 'O'. ***\n\nCurrent Suspects:\n"+"-"*17+"\n"+" ".join(sorted(clue3))+"\n"


clue4 = list(set([name for name in clue3 for letter in name if name.count(letter)==2]))
print "\n*** Clue 4: The killer's name has the same letter in it twice(two 'A's or two 'R's, etc). ***\n\nKiller Found!\n"+"-"*17+"\n"+" ".join(sorted(clue4))+"\n"
