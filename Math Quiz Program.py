import random

def cal(num,levels,method):
    correct = 0

    for i in range(num):
        try:
            num1 = random.randint(1,levels)
            num2 = random.randint(1,levels)

            if method == 4:
                operation = random.choice(ways)

            else:
                operation = ways[method-1]

            prod=str(num1)+operation+str(num2)
            prod=eval(prod)

            ans = int(raw_input("What is " + str(num1) + " " + operation + " " + str(num2) + "?\n"))

            if ans == prod:
                print "That's right -- well done.\n"

                correct += 1

            else:
                print "No, I'm afraid the answer is ", prod, ".\n"

        except:
            print "You got some errors, please check with that."
            continue

    print "\nI asked you ", num, "questions. You got ", correct, "of them right."

    if correct >= round(num*0.75):
        print "Well done!"
    elif correct >= round(num*0.5):
        print "You need more practice."
    else:
        print "Please ask your math techer for help!"

level = [("a","Beginner",10),("b","Intermediate",25),("c","Advanced",50)]

question_type = [("1","Addition"),("2","Subtraction"),("3","Multiplication"),("4","Mixed")]

ways = ["+","-","*"]

while True:
    try:

        num = int(raw_input("How many questions would you like to answer?\n"))

        if num <= 0:
            print "The number of questions must be over zero!"
            continue
        print "Please choose the level of your quiz: (Enter a, b or c)"

        for option in level:
            print option[0]+": "+option[1]
        option = raw_input()
        if option == "a":
            levels = 10
        elif option == "b":
            levels = 25
        elif option == "c":
            levels = 50
        else:
            print "You got some errors, please check with that."
            continue

        print "Please choose the operation: (Enter 1, 2, 3 or 4)"


        for option_type in question_type:
            print option_type[0]+ ": "+ option_type[1]
        method = int(raw_input())

        cal(num,levels,method)

        c=raw_input("Would you like to start another quiz? Enter Y or N\n")
        if c == "Y":
            continue
        else:
            break
    except:
        print "You got some errors, please check with that."
