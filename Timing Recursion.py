#Siyu Miao
import time
def factorial(num):
    if(num == 1):
        return 1
    else:
        return num * factorial(num - 1)

def fibonacci(num):
    if(num == 0) or (num == 1):
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

#create a function of main(upperBound).
def main(upperBound):
    while True:
        #ask user select which method to use
        method = raw_input("Please enter FIB for fibonacci or FACT for factorial: ").lower()
        #when method equal fib, then use the function of fibonacci and calculate the time, finally print the output.
        if method == "fib":
            #calcualte the beginning time.
            start = time.clock()
            #set total time equal to 0.
            total_time = 0
            #set i into fibonacci and the range.
            for i in range(1, upperBound+1):
                output = fibonacci(i)
                #calcualte the ending time.
                end = time.clock()
                #calcualte the total time.
                total_time += end - start
                print "Calculating fibonacci(" + str(i) + ") =", output, "took:", end - start, "seconds."
            print "Total time:", total_time, "seconds."
            break

        #when method equal fib, then use the function of factorial and calculate the time, finally print the output.
        elif method == "fact":
            #calcualte the beginning time.
            start = time.clock()
            #set total time equal to 0.
            total_time = 0
            #set i into factorial and the range.
            for i in range(1, upperBound+1):
                output = factorial(i)
                #calcualte the ending time.
                end = time.clock()
                #calcualte the total time.
                total_time += end - start
                print "Calculating fibonacci(" + str(i) + ") =", output, "took:", end - start, "seconds."
            print "Total time:", total_time, "seconds."
            break

        else:
            continue
while True:
    try:
        #ask user type the upper bound.
        upperBound = int(raw_input("Please enter an upper bound (int): "))
        #try function of main(upperBound).
        main(upperBound)
        break
    except:
        #if in try, user didn't type an integer, then print invalid information.
        print "That's not an integer."
        #keep asking until the user type the right input
        continue
