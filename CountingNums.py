#Siyu Miao 
#This code is for "counting number".
#Set start number, end number and the amount to count.
start_number = int(raw_input("Please enter a start number: "))
end_number = int(raw_input("Please enter an end number: "))
count = int(raw_input("Please enter the amount by which to count: "))
#When start number smaller than the end number, end number will plus one unit.
if start_number < end_number:
    for i in range(start_number, end_number+1, count):
        print "\n",i,
#When the start number bigger than the end number, end number will minus one unit.
elif start_number > end_number:
    for i in range(start_number, end_number-1, count):
        print "\n",i,
