# List and Loops
# range() method uses
for n in range(21):
    print(n)

# To find even numbers
even_numbers = []
for n in range(21):
    if n % 2 == 0:
        even_numbers.append(n)

print("Even Numbers Are:::::::",even_numbers)
# Another way is we know that we have numbers in sequence

even_numbers.clear()

for num in range(0, 21, 2):
    even_numbers.append(num)

print("even numbers are:::::::", even_numbers)

# Here is more precise one line way to write the above code which is easy to read and write.
# This method or writing code in this way is called List comprehension
even_numbers.clear()
even_numbers = [num for num in range(0,21,2)]
print("List Comprehensions::::", even_numbers)
# In case we have no idea about the sequence then,

even_numbers.clear()
even_numbers = [n for num in range(21) if num % 2 == 0]
print("List Comprehensions::::", even_numbers)

# Conditional Expression in List Comprehension
# FreeCodeCamp method

numbers = [1,2,3,4,5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

# Filtration in python-List
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def check_long_word(word):
    return len(word) > 4

long_words = list(filter(check_long_word, words))
print("Long Words:::::", long_words)

# Map method in Python-List

def incrementEachNum(num):
    return num + 1
def decrementEachNumb(num):
    return num - 1

result3 = list(map(incrementEachNum, numbers))
print("Incremented nums are:::::", result3)
result4 = list(map(decrementEachNumb, result3))
print("Decremented nums are:::::", result4)

def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        return secret_codes.append(secret_code)

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor(poem))

