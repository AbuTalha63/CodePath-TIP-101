'''
Write a function all_in() that takes in a list of integers a and a 
list of integers b as parameters. Given these two lists, return True if 
every element in list a is in list b. Return False otherwise.

1. Understand

parameters int list a & int list b
return true if a in b
else false

2. Plan
 - Define function
 - For loop iterate through list a
 - comparison operator, if a[index] == b[index]
 - return True
 - else return False

def all_in(a, b):
Example Usage:
lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))

Example Output:
True
False

3. Implement
'''
def all_in(a,b):

    for n in a:
        if n not in b:
            return False
    return True   

lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))

'''
Write a function create_dictionary() that takes in a list of keys and a 
list of values as parameters. The function returns a dictionary where each 
item in keys is paired with a corresponding item in values.

keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). 
You may assume keys and values are the same length.

1. Understand:
- 2 lists keys and values
- return a dictionary where each keys address to each value

2. Plan:
- define a function
- create a empty dictinary
- check if length of keys and values are equal, if not then return an empty dictionary
- for loop from 0 to length of list keys (or values)
- add each keys (keys[i]) address to each values (values[i])
- return the dictionary

def create_dictionary(keys, values):
    pass
    
Example Input:
keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']

Example Output:
{'peanut': 'butter', 'dragon': 'fly', 'star': 'fish', 'pop': 'corn', 'space': 'ship'}
'''

def create_dictionary(keys, values):
    result = {}
    if len(keys) != len(values):
        return result
    
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    
    return result

keys = ['peanut', 'dragon', 'star', 'pop', 'space']

values = ['butter', 'fly', 'fish', 'corn', 'ship']
print(create_dictionary(keys, values))

'''
Write a function print_pair() that takes in a dictionary 
dictionary and a key target as parameters. The function looks for the target and 
when found, it prints the key and it's associated value as "Key: <key>" followed 
by "Value: <value>". If target is not in dictionary, print "That pair does not exist!".

def print_pair(dictionary, target):
    pass
    
    
Example Usage:

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
Example Output:

Key: patrick
Value: star
That pair does not exist!
Key: spongebob
Value: squarepants

1. Understand
 - I/O: 1 dictionary, string (which is the key), output: the key and value pair
 

2. Plan
 - Define funtion
 - For each loop iterating through dictionary, at that key in the dictoriary, looks at the value
    - if that value is equal to the target parameter passed, return both key and value
'''

def print_pair(dictionary, target):
    for key in dictionary:
        if key == target:
            print("key: " , key)
            print("Value: " , dictionary[key])
            return

    print("that pair does not exist")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")