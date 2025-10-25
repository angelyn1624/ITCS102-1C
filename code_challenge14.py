anime_list = []

while True:
	anime = input("Enter the title of an anime (or type 'exit' to finish): ")
	if anime == "exit":
		break
	anime_list.append(anime)
	print(anime, " has been added to your anime list.")

print("\nyou have exited the anime program.")
print("your anime list includes:")
for b in anime_list:
	print("-", b)

