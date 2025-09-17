#give the factor of 10

number = eval(input("enter a number"))
factor = 1
for x in range(number, 0,-1):
	factor *= x
print("the factor of",number,"is",factor)
	