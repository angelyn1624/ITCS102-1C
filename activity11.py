temp = eval(input("Enter temperature outside-->"))

#input 33
if temp >= 1 and temp <= 20:
	print("temperature is Considered as Extremely cold")
elif temp >= 21 and temp <= 30:
	print("Temperature is Considered as Moderately Cold")
else:
	print("Invalid temperature")