# Luke Colvin
# Comp 120
# Lab 5
# Program Version 2

def inputSales():
    
    # Function to input daily sales values from the user. Returns a list of sales values.
    sales = []
    while True:
        if (sale := input("Enter the daily sales or -1 to exit: ")) == '-1':
            break
        sales.append(float(sale))
    return sales

def calculateTotalSales(sales):
    
    # Function to calculate the total sales from a list of sales values. Returns the total sales.
    totalSales = 0
    for sale in sales:
        totalSales += sale
    return totalSales

def calculateAverageSales(totalSales, days):

    # Function to calculate the average sales from the total sales and number of days. Returns the average sales rounded to the hundredths place.
    averageSales = round(totalSales / days, 2)
    return averageSales

def outputSales(sales):
    
    # Function to output individual sales from a list of sales values.
    print("Individual sales for each day:")
    for sale in sales:
        print(sale)

def outputTotalSales(totalSales):
    
    # Function to output the total sales.
    print("Total sales for the period:", totalSales)

def outputAverageSales(averageSales):
    
    # Function to output the average sales.
    print("Average daily sales:", averageSales)

# Main program
sales = inputSales()
totalSales = calculateTotalSales(sales)
days = len(sales)
averageSales = calculateAverageSales(totalSales, days)

outputSales(sales)
outputTotalSales(totalSales)
outputAverageSales(averageSales)
