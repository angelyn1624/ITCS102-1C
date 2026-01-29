name = (input("Enter a word?: "))

num = [] 
for a in range(1,7,):
    num1 = int(input(f"Enter number {a}: "))
    num.append(num1)
print(num)


length = len(name)
average = sum(num) / len(num)

print("the length of the word is" ,length)
print("the average of the number is",average)

if length < average:
        print(f"The length of the word '{name} is less than the average")
    
else:
      print("The length of the word is equal to the average")


