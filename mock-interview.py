'''
Problem #1 - Find the Index of the First Occurrence in a String
Write a function that, when given two strings, needle and haystack, 
returns the index of the first occurrence of needle in haystack, or 
returns -1 if needle is not part of haystack.

example usage;
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Input: haystack = "leetcode", needle = "leeto"
Output: -1

UPI method

1. Understand
 - input: 2 strings, needle and haystack
 - output: integer; specefically the index of the start of the first occurcne in the haystack string
 - edge cases: repeats of the needle, spaces in either string
 - no match means return -1
 
2. Plan
 - Define the function, 2 parameters
 - if needle in haystack then; compare needle [0] haystack, and return the first 
        occurence of needle [0] from haystack
 - else: return -1
 

3. Implement
'''
def needle_finder(needle, haystack):
    if needle in haystack:
        for char in haystack:
            if (char == needle[0]):
                return indexof(char)
    else:
        return -1
    
haystack = "sadbutsad"
needle = "sad"
print(needle_finder(needle, haystack))

