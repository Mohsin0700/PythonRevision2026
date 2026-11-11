# String slicing lets you extract a portion of a string or work with only a specific part of it. Here's the basic syntax:
# string[start:stop]
my_name = "Mohsin_Hussain"
print(my_name[1:10])
print(my_name[:6])
print(my_name[6:])
print(my_name[0: -1: 3])
# A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, and leaving start and stop blank:

print(my_name[::-1])
greeting = 'Hello'
print(greeting[2:])
