#Siyu Miao
import random
#Define the car's obejects
class Car(object):
    """A virtual race car"""

    def __init__(self, make="BMW"):
        #constructor
        self.miles = 0
        self.make = make

    def __str__(self):
        reply = " has driven "+str(self.miles) +" miles."
        return reply
    
    def info(self):
        print "This race car is a", self.make + "."
        print "It has", self.miles, "miles on it."

    def drive(self,type):
        if type == "Ferrari":
            self.miles += random.randrange(10,90)
        if type == "Porsche":
            self.miles += random.randrange(30,70)
        if type == "BMW" :
            self.miles += 50


# main
print "Welcome to the race!"
print "-"*60
print "Each player,please select your car and driver."
print "Cars are 'BMW,Porsche,and Ferrari'"
print "Drivers are 'Mario Andretti and Tony Stewart'"
cars=["BMW","Porsche","Ferrari"]
drivers=["Mario Andretti","Tony Stewart"]
#While the car in the dictionary
while 1:
    car1 = raw_input("\nPlayer 1, please enter your car: ")
    if car1 in cars:
        break
    else:
        print "Choose the wrong car!"
#While the driver in the dictionary
while 1:
    driver1 = raw_input("Player 1, please enter your driver: ")
    if  driver1 not in drivers:
        print "Choose the wrong driver!"
    else:
        break
#While the car in the dictionary
while 1:
    car2 = raw_input("Player 2, please enter your car: ")
    if car2 in cars:
        break
    else:
        print "Choose the wrong car！"
#While the driver in the dictionary
while 1:
    driver2 = raw_input("Player 2, please enter your driver: ")
    if  driver2 not in drivers:
        print "Choose the wrong driver！"
    else:
        break

player1 = Car(car1)
player2 = Car(car2)

i = 1
#Print the game
while 1:
    #i = 1
    print "Lap:",i
    player1.drive(car1)
    player2.drive(car2)
    print "player1",player1
    print "player2",player2
    i += 1
    #print player1.miles,player2.miles
    if player1.miles >= 500 or player2.miles >= 500:
        if player1.miles > player2.miles:
            print "Congratulations! Player 1 with",driver1,"driving a",car1, ", you are the winner!"
            break
        else:
            print "Congratulations! Player 2 with",driver2,"driving a",car2, ", you are the winner!"
            break
