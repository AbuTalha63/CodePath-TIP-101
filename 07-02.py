# July 2nd
# --- Q  --- #

# July 2nd - Session 1 - TIP 101 - Breakout room 9

'''
1. understand


2. plan 

'''







# def count_mississippi(limit):
#     for num in range(1, limit):
#         print( f"{num} mississippi")
        
# count_mississippi(6)



# - 2 - #
"""
Understand - 
   Input- String
   Output- String
   Edge cases- empty strign, diff data type, string length of 1.
   
 

Plan:
Define the function
if the string has one or zero characters then reject it (edge case)
intialize empty dictionary




Implement - """

""""""
# def swap_ends(my_str):
#     if len(my_str) <= 1:
#         return my_str

#     return my_str[-1] + my_str[1:-1] + my_str[0]
        
# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)

# --- Question 3 --- #

'''
1. Understand
 - input: string
 - output: True/False
 - case-sensitive
 
2. Plan
 - create a string containing all 26 letters of the alphabet
 - loop through the string
 - if not in alphabet string variable, return False
 - else return true
 
3. Implement
'''

def is_pangram(my_str):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"
    
    for letter in alphabet:
        if letter not in my_str:
            return False
        return True
    
my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))


# --- Question 4 --- #

'''
Write a function reverse_string() that takes a string my_str as a
parameter and returns the string reversed.
'''

def reverse_string(my_str):
    return my_str[::-1]

my_str = "live"
print(reverse_string(my_str))


# --- Question 5 --- #
'''
Write a function first_unique_char() that given a string my_str as a parameter, 
it finds the first non-repeating character in it and returns its index. If it does 
not exist, then return -1.
'''


"""
Understand - 
1. input : string and output: integer 
 papamter: find the frist

"""
# def first_unique_char(my_str):
#     for char in my_str:
#         if my_str.count(char) == 1:
#             return my_str.index(char)
            
#     return -1


# --- Question 6 --- #

'''
Write a function min_distance() that takes in a list of strings words and 
two strings word1 and word2 as parameters. The function should return the 
minimum distance between word1 and word2 in the list of words. The distance 
between one word and an adjacent word in the list is 1.

1. Understand
 - list, two words
 - output int representing the distance
 - edge case: word passed in the parameter does not exist, empty list. 
2. Plan
 - Define function
 - 
3. Implement
'''

def min_distance(words, word1, word2):
     index1 = -1
     index2 = -1
     min_dist = len(words)
    
     for i in range(len(words)):
        if words[i] == word1:
            index1 = i

        if words[i] == word2:
            index2 = i

        if index1 != -1 and index2 != -1:
            distance = abs(index1 - index2)
            if distance < min_dist:
                min_dist = distance       

     return min_dist
    


words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)




    
    
    
    
# testString = "Hello"

# if my_str is not in testString:
    

    
    
    
    
    
    


# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))    


