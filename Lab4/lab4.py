# Luke Colvin
# Comp 120
# Lab 4
# Version 1

# Initialize an empty list for daily sales
sales = []

# Input sales values from the user
while True:
    sale = input("Enter the daily sales or -1 to exit: ")

    # Check for sentinel value
    if sale == '-1':
        break

    # Convert the input to a float and append to the sales list
    sales.append(float(sale))

# Initialize variables for total sales and count of days
totalSales = 0
days = 0

# Run through the list to calculate total sales
for sale in sales:
    totalSales += sale
    days += 1

# Calculate the average sales then rounds the result to the hundredths place
averageSales = round(totalSales / days, 2)

# Output individual sales from list
print("Individual sales for each day:")
for sale in sales:
    print(sale)


# Output total sales and average sales
print("Total sales for the period: ", totalSales)
print("Average daily sales: ", averageSales)

