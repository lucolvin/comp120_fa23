# Luke Colvin
# Comp 120
# Lab 3
# Version 1

#Declare variable
steakTemp = 0

steakTemp = float(input("Please enter Steak temperature. "))

#statement for rare
if steakTemp >= 125 and steakTemp < 145:
    print("Your steak is cooked to rare.")

#statement for medium
elif steakTemp >= 145 and steakTemp < 160:
    print("Your steak is cooked to medium.")

#statement for well done
elif steakTemp >= 160 and steakTemp <= 200:
    print("Your steak is cooked to well done.")

#Add an extra statement for burnt just for fun
elif steakTemp > 200:
    print("Your steak is overcooked.")

#provide an statement to cover lower temps
else:
    print("Your steak is raw.")     

