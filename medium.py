col = eval(input("enter a number of columns: "))

for a in range(1,11,1):
	for b in range(1, col +1, 1):
		print(f"{a}x{b}={a*b}", end="\t\t")
	print()


for a in range(1,6,1):
	for c in range(6,a,-1):
		print(" ", end="")
	for d in range(1,a+1 , 1):
		print("*", end=" ")
	print()