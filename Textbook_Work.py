vatTemp = 0

vatTemp = float(input("Input vat temp"));
while vatTemp >= 102.5:
    print("turn down the thermostat wait 5 minutes and try again");
if vatTemp < 102.5:
    print("Temp is acceptable check again in 15 minutes");
    
