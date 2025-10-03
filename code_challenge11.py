print("\t\t *" , end=" ")
for x in range(1,11,1):
	for y in range(10,x,-1):
		print(" ", end=" ")
	for u in range(1,x,1):
		print("*", end=" ")
	for i in range (1,x,1):
		print("*", end=" ")
	print()

#half
for x in range(1,11,1):
	for y in range(1,x,1):
		print(" ", end=" ")
	for u in range(10,x,-1):
		print("*", end=" ")
	for i in range (10,x,-1):
		print("*", end=" ")
	print("*")