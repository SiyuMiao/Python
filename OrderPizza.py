#Siyu Miao
people = int(raw_input("How many people do you expect? "))
original_number = pizza = (people*80)/(3.1415*49)
rounded_up_pizza = int(original_number+1)-int(1-original_number+int(original_number))
original_number = soda = (people*0.5)/2
rounded_up_soda = int(original_number+1)-int(1-original_number+int(original_number))
subtotal = rounded_up_pizza*11.99+rounded_up_soda*1.99
total_cost_after_tax = subtotal*0.07+subtotal
print "\nI recommend ordering:""\n-", rounded_up_pizza, "14-inch pizza(s)","\n-",rounded_up_soda, "2-liter bottle(s) of soda","\n""\nSubtotal: $",subtotal,"\nTotal cost after tax = $", "%.2f"% total_cost_after_tax
