# Mock Interview - 10/29/2026


'''
Problem #2 - Longest Common Prefix
Write a function that returns the longest common prefix string amongst
an array of strings strs.
If there is no common prefix, return an empty string "".
Input: strs = ["flower","flow","flight"]
Output: "fl"
Input: strs = ["dog","racecar","car"]
Output: ""

Understand:
 - Only prefix commonality
 - Input: list of strings
 - One string that is the common prefix
Test Cases;
 - 

Plan
 - Create the function
 - Iterate through the list
 - If 

Implement
''' 

strs = ["flower","flow","flight"]
def commonPrefix (strs):
    refrence = strs[0] # this points to "flower"

    for index in range(len(refrence)): # looping through the word "flower" & assigning index to each of the chars
        for i in range(1, len(strs)): # looping through the other words in the list
            word = strs[i]
            if (index >= len(word) or refrence[index] != word[index]):
                return refrence[:index]

result = commonPrefix(strs)
print(result)