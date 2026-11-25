#region ---------- UNIT 2 SESSION 1 PROBLEM SET VERSION 1 ---------- #

# AI DISCLOSURE: The problems in this file were formatted with the help of
# AI (Claude, by Anthropic). The problems come from CodePath TIP101
# (Unit 2, Session 1).

#region Problem 1: All In
'''
PROBLEM 1: All In
Write a function all_in() that takes in a list of integers a and a list of
integers b as parameters. Given these two lists, return True if every element
in list a is in list b. Return False otherwise.
'''
def all_in(a, b):
    for item in a:
        if item not in b:
            return False
    return True
# Example Usage:
lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))
# Example Output:
    # True
    # False
# more tests from me
all_in([], [1,2]) # should return False
#endregion



#region Problem 2: Create a Dictionary
'''
PROBLEM 2: Create a Dictionary
Write a function create_dictionary() that takes in a list of keys and a list
of values as parameters. The function returns a dictionary where each item in
keys is paired with a corresponding item in values.
keys[i] should be paired with values[i] in the dictionary where
0 <= i <= len(keys). You may assume keys and values are the same length.
'''
def create_dictionary(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary
# Example Input:
keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
print(create_dictionary(keys, values))
# Example Output:
#     {'peanut': 'butter', 'dragon': 'fly', 'star': 'fish', 'pop': 'corn', 'space': 'ship'}
#endregion



#region Problem 3: Print Pair
'''
PROBLEM 3: Print Pair
Write a function print_pair() that takes in a dictionary dictionary and a key
target as parameters. The function looks for the target and when found, it
prints the key and its associated value as "Key: <key>" followed by
"Value: <value>". If target is not in dictionary, print
"That pair does not exist!".
'''
def print_pair(dictionary, target):
    if target in dictionary:
        print(f"Key: {target}")
        print(f"Value: {dictionary[target]}")
    else:
        print("That target does not exist!")
# Example Usage:
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
# Example Output:
#     Key: patrick
#     Value: star
#     That pair does not exist!
#     Key: spongebob
#     Value: squarepants
#endregion



#region Problem 4: Keys Versus Values
'''
PROBLEM 4: Keys Versus Values
Write a function keys_v_values() that takes in a dictionary dictionary whose
keys and values are both integers. Using at least one loop, the function
should find the sum of all keys in the dictionary and the sum of all values.
If the sum of all keys is greater than the sum of all values, the function
should return the string "keys".
If the sum of all values is greater than the sum of all keys, the function
should return the string "values".
If keys and values have equal sums, the function should return the string
"balanced".
'''
def keys_v_values(dictionary):
    key_total = 0
    value_total = 0
    for key, value in dictionary.items():
        if key > value:
            key_total += key
        elif value > key:
            value_total += value
    if key_total > value_total:
        return "keys"
    elif value_total > key_total:
        return "Values"
    else:
        return "balanced"
# Example Usage:
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)
dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)
# Example Output:
#     values
#     keys
#endregion



#region Problem 5: Restock Inventory
'''
PROBLEM 5: Restock Inventory
Write a function restock_inventory() that updates an inventory dictionary
based on a restock list. It accepts two parameters:
  - current_inventory: a dictionary where each key-value pair represents an
    item and its current stock in the inventory
  - restock_list: a dictionary where each key-value pair represents an item
    and the quantity to be added to the inventory
If an item in restock_list is not present in the current_inventory, it should
be added. The function should return the updated dictionary
current_inventory.
'''
def restock_inventory(current_inventory, restock_list):
    # for key in current_inventory:
    #     if key in restock_list.keys():
    #         current_inventory[key] += restock_list[key]
    #     else:
    #         current_inventory[restock_list.get(key)] = restock_list[key]
    # return current_inventory
    for item, quantity in restock_list.items():
        # if item in current_inventory.keys():
        current_stock = current_inventory.get(item, 0)
        quantity += current_stock
        
# Example Input:
current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}
restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

# Example Output:
#     {
#         "apples": 40,
#         "bananas": 15,
#         "oranges": 30,
#         "pears": 5
#     }
#endregion



#region Problem 6: Calculate GPA
'''
PROBLEM 6: Calculate GPA
Write a function calculate_gpa() that calculates the grade point average
(GPA) for a student based on their course grades and returns the gpa as a
float. The function takes in a dictionary report_card as a parameter where
each key-value pair represents a course and the grade received in that
course respectively. The grades are represented as strings
("A", "B", "C", "D", "F") and each grade corresponds to a certain number of
grade points:
    "A" = 4
    "B" = 3
    "C" = 2
    "D" = 1
    "F" = 0
A GPA is calculated by finding the average of all grade points.
'''
# def calculate_gpa(report_card):
#     pass
# Example Usage:
# report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
# print(calculate_gpa(report_card))
# Example Output:
#     3.3333333333333335
#endregion



#region Problem 7: Best Book
'''
PROBLEM 7: Best Book
Imagine you are working on a book review software like Goodreads. Write a
function named highest_rated() that returns the book with the highest rating.
The function should take in a list of dictionaries named books as a
parameter. Each dictionary represents data associated with a book, including
its title, author, and rating. The function should return the dictionary for
the book with the highest rating.
'''
# def highest_rated(books):
#     pass
# Example Input:
# books = [
#     {"title": "Tomorrow, and Tomorrow, and Tomorrow",
#      "author": "Gabrielle Zevin",
#      "rating": 4.18
#     },
#     {"title": "A Fortune For Your Disaster",
#      "author": "Hanif Abdurraqib",
#      "rating": 4.47
#     },
#     {"title": "The Seven Husbands of Evenlyn Hugo",
#      "author": "Taylor Jenkins Reid",
#      "rating": 4.40
#     }
# ]
# Expected Output:
#     {"title": "A Fortune For Your Disaster",
#      "author": "Hanif Abdurraqib",
#      "rating": 4.47
#     }
#endregion



#region Problem 8: Index-Value Map
'''
PROBLEM 8: Index-Value Map
Write a function index_to_value_map() that takes in a list lst and returns a
dictionary that maps the index of each element in lst to its value.
'''
# def index_to_value_map(lst):
#     pass
# Example Input:
# lst = ["apple", "banana", "cherry"]
# Example Output:
#     {0: "apple", 1: "banana", 2: "cherry"}
#endregion



#endregion



#region ---------- UNIT 2 CHEATSHEET ---------- #
'''
UNIT 2 CHEATSHEET
In-Scope: may appear on the assessment
Not In-Scope: useful, but not required
Unit Goals
  - Create and modify a dictionary
  - Access and loop over keys, values, and key-value pairs in a dictionary
  - Solve problems using frequency maps
  - Solve problems involving lists, dictionaries, or a combination of both
------------------------------------------------------------
BUILT-IN FUNCTIONS
------------------------------------------------------------
Type Casting: transforming data from one type into another.
int(x)    Cast a float or string to an integer. Floats are rounded down.
    x = int(2.5)         # 2
    y = int("5")         # 5
float(x)  Cast an integer or string to a floating point number.
    x = float(2)         # 2.0
    y = float("5")       # 5.0
    z = float("5.3")     # 5.3
str(x)    Transform a data type into a string. x can also be a more complex
          type like a list or dictionary.
    x = str(2)           # "2"
    y = str(2.0)         # "2.0"
    z = str([1, 2, 3, 4])  # "[1, 2, 3, 4]"
Remainder Division
The % operator (modulo) returns the remainder after dividing x by y.
    print(5 % 2)         # 1 because 5 / 2 = 2 remainder 1
    print(10 % 2)        # 0 because 10 / 2 = 5 remainder 0
sum(x)    Returns the sum of all values in a list.
    sum([1, 2, 3, 4])    # 10
min(x)    Returns the argument or list item with the lowest value.
    min([2, 3, 4, 1, 5])                      # 1
    min(5, 2, 3)                              # 2
    min(['a', 'b', 'c', 'aa'])                # 'a'
    min({'a': 1, 'b': 2, 'c': 3, 'd': 4})     # 'a' (smallest key)
max(x)    Returns the argument or list item with the highest value.
    max([2, 3, 5, 1, 4])                      # 5
    max(5, 2, 3)                              # 5
    max(['a', 'b', 'c', 'aa'])                # 'c'
    max({'a': 1, 'b': 2, 'c': 3, 'd': 4})     # 'd' (largest key)
------------------------------------------------------------
DICTIONARY METHODS & SYNTAX
------------------------------------------------------------
Setting and Updating Values
Use the assignment operator =. If the key does not exist, a new key-value
pair is added.
    d = {'a': 1, 'b': 2, 'c': 3}
    d['d'] = 4           # Adds a new key 'd' with value 4
    print(d)             # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    d['a'] = 100         # Updates the value of key 'a'
    print(d)             # {'a': 100, 'b': 2, 'c': 3, 'd': 4}
Accessing Elements
Method 1: direct access with []. Raises a KeyError if the key is not found.
    d = {'a': 1, 'b': 2, 'c': 3}
    print(d['a'])        # 1
    print(d['b'])        # 2
Method 2: d.get(key, default_val), a safer way to access values.
  - key: the key of the value you want (required)
  - default_val: returned if the key does not exist (optional, defaults to None)
    d = {'a': 1, 'b': 2, 'c': 3}
    print(d.get('a'))                  # 1
    print(d.get('z'))                  # None
    print(d.get('z', 'Not Found'))     # 'Not Found'
d.pop(key, default_val)
Removes an item and returns its value.
  - key: the key of the item to remove (required)
  - default_val: returned if the key does not exist (optional). Without it, a
    missing key raises an error.
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    d.pop('a')           # Returns 1
    print(d)             # {'b': 2, 'c': 3, 'd': 4}
    d.pop('e')           # Raises KeyError
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    d.pop('a', None)     # Returns 1
    d.pop('e', None)     # Returns None, d unchanged
d.keys()      Returns the keys in the dictionary.
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    print(d.keys())      # ['a', 'b', 'c', 'd']
d.values()    Returns the values in the dictionary.
    print(d.values())    # [1, 2, 3, 4]
d.items()     Returns the key-value pairs as tuples.
    print(d.items())     # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
------------------------------------------------------------
BONUS CONCEPTS (Not In-Scope)
------------------------------------------------------------
remove(x)      Removes first element with value x from list
zip()          Iterate over multiple lists, dictionaries, or other iterables
               simultaneously
defaultdict()  Dictionary with default values for new or missing keys
               (helps avoid KeyErrors)
d.copy()       Returns a copy of the dictionary d
sorted(x)      Returns a copy of the given iterable sorted in ascending order
'''
#endregion