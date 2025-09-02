name = input("please input your name --> ")
fare = eval(input("fare fee -->"))
isStudent = input("are you currently a student (yes/no)")

if isStudent == "yes":
	discount = fare * 0.2
	new_fare = fare - discount
	print("Hi",name," your discount is ", discount,"your new fare is ", new_fare)
else:
	print("hi",name," your only elegible for regular price , ")
