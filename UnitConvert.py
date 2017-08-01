#Siyu Miao
#This code is for the "units change" between L, ml, G and t, I write the code for each units, and then change to the other units.
convert_from = raw_input("Which unit would you like to convert from? ")
convert_to = raw_input("Which unit would you like to convert to? ")
value = float(raw_input("Enter your value: "))

ml_to_L = value/1000
G_to_L = value/0.2641721
t_to_L = value/202.884

L_to_ml = value*1000
L_to_G = value*0.2641721
L_to_t = value*202.884

#From L to the other units
if convert_from == "L":
    if convert_to == "L":
        print "Thanks!", value, "L is equal to", value, "L"
    elif convert_to == "ml":
        print "Thanks!", value, "L is equal to", L_to_ml, "ml"
    elif convert_to == "G":
        print "Thanks!", value, "L is equal to", L_to_G, "G"
    elif convert_to == "t":
        print "Thanks!", value, "L is equal to", L_to_t, "t"
    else:
        print "Invalid units! The units of 'L', 'ml', 'G' and 't' are valid!"
#From ml to the other units.
elif convert_from == "ml":
    if convert_to == "L":
        print "Thanks!", value, "ml is equel to", ml_to_L, "L"
    elif convert_to == "ml":
        print "Thanks!", value, "ml is equal to", value, "ml"
    elif convert_to == "G":
        print "Thanks!", value, "ml is equal to", float(ml_to_L)*0.2641721, "G"
    elif convert_to == "t":
        print "Thanks!", value, "ml is equal to", float(ml_to_L)*202.884, "t"
    else:
        print "Invalid units! The units of 'L', 'ml', 'G' and 't' are valid!"
#From G to the other units.
elif convert_from == "G":
    if convert_to == "L":
        print "Thanks!", value, "G is equal to", G_to_L, "L"
    elif convert_to == "ml":
        print "Thanks!", value, "G is equal to", float(G_to_L)*1000, "ml"
    elif convert_to == "G":
        print "Thanks!", value, "G is equal to", value, "G"
    elif convert_to == "t":
        print "Thanks!", value, "G is equal to", float(G_to_L)*202.884, "t"
    else:
        print "Invalid units! The units of 'L', 'ml', 'G' and 't' are valid!"
#From t to the other units.
elif convert_from == "t":
    if convert_to == "L":
        print "Thanks!", value, "t is equal to", t_to_L, "L"
    elif convert_to == "ml":
        print "Thanks!", value, "t is equal to", float(t_to_L)*1000, "ml"
    elif convert_to == "G":
        print "Thanks!", value, "t is equal to", float(t_to_L)*0.2641721, "G"
    elif convert_to == "t":
        print "Thanks!", value, "t is equal to", value, "t"
    else:
        print "Invalid units! The units of 'L', 'ml', 'G' and 't' are valid!"
else:
    print "Invalid units! The units of 'L', 'ml', 'G' and 't' are valid!"
        
