#Siyu Miao
# Write the function of noun and let it random from the list.
def random_noun():
    import random
    return random.choice(["bread","juice","tiger","monkey","desk"])
# Write the function of verb and let it random from the list.
def random_verb():
    import random
    return random.choice(["ate","walked","took","bought","did"])
# Write the function of adjective and let it random from the list.
def random_adjective():
    import random
    return random.choice(["ugly","green","black","white","red"])
# Write the function of sentence, put all the functions together.
def random_sentence():
    return "The" + " " + random_adjective() + " " + \
           random_noun()+ " " + random_verb() + " " + \
           "the" + " " + random_adjective() + " " + random_noun()+ "."


sentences = int(raw_input("How many sentences would you like in your essay? "))
# Write the function of essay, and ask user how many sentences in the essay.
def random_essay():
    essay = ""
    i = 0
    while i < sentences:
        essay += "\n" + random_sentence()
        i += 1
    return essay
# Print essay
print "Here's your automatically_generated essay: "
print random_essay()
