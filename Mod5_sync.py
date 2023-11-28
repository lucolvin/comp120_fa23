#Luke Colvin
#10-30-2023
#Thine calorie counter of the very food of which we partake
#Create lists to hold our data

foodItems = []
foodCalories = []

#input for calories or to exit
foodCal = int(input("please input calories or 0 to exit"))
while foodCal != 0:

    #Input for food name 
    food = input("please enter food name")

    #assign values to list
    foodItems.append(food)
    foodCalories.append(foodCal)

    #Re-prompt for calsories or to exit
    foodCal = int(input("please input calories or 0 to exit"))

#calories total
totalCals = 0
for cal in foodCalories:
    totalCals = totalCals + cal

print ("The total of all of the calories is",totalCals)

#print items we ate with calories
for i in range(len(foodItems)):
    print("Food Item: ",foodItems[i], " Calories: ",foodCalories[i])
