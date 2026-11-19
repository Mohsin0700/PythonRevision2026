# We'll be practicing lists, loops and iterators in this folder.
name = "Mohsin"
# creating a list using a constructor that takes an iterable as as argument
charList = list(name)
print("Name as list:::::::::::::::",charList)
# deleting an element from the list
del charList[1]
print("List after deleting 'o' :::::", charList)
# Checking if an element exists in the list
is_exist = 'o' in charList
print("Is 'o' exists in the list::::::", is_exist)
# Un-packing a list
my_details = ["Mohsin", 26, True]
my_name, my_age, is_developer = my_details
print(f"Hi!, My name is {my_name} and I'm {my_age} years old. I'm a developer it's {is_developer}")
# remaining elements can also be stored.
a, *b = my_details
print(f"Value of a:{a}---Value of b:{b}")
# Sorting a list
ages = [32,46,15,7,11,19]
# ages.sort() # This method sorts the originol List
print(ages)
newAges = sorted(ages) #This method does not mofify the original list, it creates and return a new List
print(f"Original List::: {ages}", f"New List without touching original one:::{newAges}")
