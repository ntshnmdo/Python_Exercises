name, char = input("enter comma separated name and character : ").split(",")
print(f"length of the name is : {len(name.strip())}")
# we can also use strip methods for removing spaces 
print(f"character count : {name.strip().lower().count(char.strip().lower())}")