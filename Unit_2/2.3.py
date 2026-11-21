''' Write a function return_book() that accepts a string title and 
a dictionary library as parameters. library maps book titles to the 
number of copies the library currently has in stock. The function should increment the 
quantity of the book title in library by 1. If title is not in the library, 
then add it and set quantity to 1. Return the updated library dictionary.

def return_book(title, library):
    pass
Example Usage:

library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)

updated_lib = return_book("The Giver", library)
print(updated_lib)

Understand: Create a function that takes a book title and a library dictionary, 
updates the quantity of the book in the library, and returns the updated dictionary.
Plan:
- Create a function return_book that takes two parameters: title and library.
- Create a empty dictionary to store the updated library.
- Create a loop to iterate through the library dictionary.
- If the title is found in the library, increment its quantity by 1.
- If the title is not found, add it to the library with a quantity of 1
- Return the updated library dictionary.
Input: A string title and a dictionary library.
Output: The updated library dictionary.
'''
# Impelementation

def return_book(title, library):
    if title in library:
        library[title] += 1
    else:
        library[title] = 1
    return library
    

library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

updated_lib = return_book("1984", library)
print(updated_lib)

updated_lib = return_book("The Giver", library)
print(updated_lib)

# --- Q2 --- #

def dict_difference(d1, d2):
    new_dict = {}
    for key, value in d1.items():
        if d2.get(key) != value:
            new_dict[key] = value
    return new_dict
    
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 2, 'd': 1}
print(dict_difference(d2, d1))

# --- Q3 --- #
