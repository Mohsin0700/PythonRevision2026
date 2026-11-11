# isinstance method in pythong
account_balance = '56800'
if(isinstance(account_balance, (int, float))):
    print(account_balance / 2)

print("Account Balance is not a number")

# in method for Strings in python

my_name = "Mohsin"
print("Moh" in my_name)
print("hom" in my_name)
print("M" in my_name)
print("m" in my_name) # String "M" & "m" is considered different in python...

# To find length of a string

print(len(my_name))
# Getting a character using it's index
# print(my_name[6]) # it' will through an error
print(my_name[5])
my_name_length = len(my_name) 
print(my_name[my_name_length - 1]) # Jugarr for other languages
print(my_name[-1]) # Python's power, recommended
