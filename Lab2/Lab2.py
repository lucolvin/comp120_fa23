# Input customer's first name and last name
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")

# Concatenate the first and last names
fullName = firstName + " " + lastName

# Input the amount of a retail sale
saleAmount = float(input("Enter the amount of the retail sale: "))

# Calculate tax amount (tax rate is 0.0625)
taxRate = 0.0625
taxAmount = saleAmount * taxRate

# Calculate gross sale (sale amount + tax amount)
grossSale = saleAmount + taxAmount

# Output customer's full name, net sale, tax amount, and gross sale
print("Full Name:", fullName)
print("Net Sale Amount:", saleAmount)
print("Tax Amount:", taxAmount)
print("Gross Sale Amount:", grossSale)
