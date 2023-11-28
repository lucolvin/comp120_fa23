pocketMoney = 0
hasCar = "n"
#prompt and accept input for
#money
pocketMoney = float(input("How much money is in your wallet?"))
if pocketMoney > 10: 
    hasCar = input("Do you have a car? y/n")
    if hasCar =="y":
        print("Let's go to Chick-Fil-A")
    else:
        print("Let's eat at Luddy")
else:
    print("Let's eat at Luddy")

        
