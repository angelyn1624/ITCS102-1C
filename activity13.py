#Ask user to input number
#after get the summation of all the number provided 

sum = 0 
for x in range(1,11,1):
	
	print(x)
	number = eval(input("Enter your number"))
	sum += number
print("\n\tthe sum of all the number giveen is",sum)
