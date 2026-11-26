#region ---------- UNIT 3 SESSION 2 PROBLEM SET VERSION 1 ---------- #
# AI DISCLOSURE: The problems in this file were formatted with the help of
# AI (Claude, by Anthropic). The problems come from CodePath TIP101
# (Unit 3, Session 2).


#region Problem 1: Sum of Strings
'''
PROBLEM 1: Sum of Strings
Write a function sum_of_number_strings() that takes in a list of strings
nums. Each string is a representation of an integer. The function should
return the sum of these strings as an integer.
'''
# def sum_of_number_strings(nums):
#     pass
# Example Usage:
# nums = ["10", "20", "30"]
# total = sum_of_number_strings(nums)
# print(total)
# Example Output:
#     60
#endregion



#region Problem 2: Remove Duplicates
'''
PROBLEM 2: Remove Duplicates
Write a function remove_duplicates() that takes in a sorted list of integers
nums as a parameter and removes all duplicates in the list. The function
returns the modified list.
'''
# def remove_duplicates(nums):
#     pass
# Example Usage:
# nums = [1, 1, 1, 2, 3, 4, 4, 5, 6, 6]
# no_dups = remove_duplicates(nums)
# print(no_dups)
# Example Output:
#     [1, 2, 3, 4, 5, 6]
#endregion



#region Problem 3: Reverse Letters
'''
PROBLEM 3: Reverse Letters
Write a function reverse_only_letters() that takes in a string s as a
parameter. The function reverses the order of the letters in the string and
returns the new string. Non-letter characters should remain in their original
positions.
'''
# def reverse_only_letters(s):
#     pass
# Example Usage:
# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)
# Example Output:
#     j-Ih-gfE-dCba
#endregion



#region Problem 4: Longest Uniform Substring
'''
PROBLEM 4: Longest Uniform Substring
Write a function longest_uniform_substring() that takes in a string s and
returns the length of the longest uniform substring. A uniform substring
consists of a single repeated character.
'''
# def longest_uniform_substring(s):
#     pass
# Example Usage:
# s1 = "aabbbbCdAA"
# l1 = longest_uniform_substring(s1)
# print(l1)
# s2 = "abcdef"
# l2 = longest_uniform_substring(s2)
# print(l2)
# Example Output:
#     4
#     1
#endregion



#region Problem 5: Teemo's Attack
'''
PROBLEM 5: Teemo's Attack
In the game League of Legends, Teemo attacks his enemy Ashe with poison
arrows. Write a function find_poisoned_duration() that takes in two
parameters: time_series (the times at which Teemo's attacks hit Ashe) and
duration (the duration of the poisoning effect). The function returns the
total time that Ashe is in a poisoned condition.
time_series is a list of integers that represents the times at which Teemo
attacks and makes Ashe poisoned for the exact duration.
If Teemo hits Ashe while she is still poisoned, the poison's duration starts
over. For example, if Teemo attacks at times 1 and 4 for 3 seconds, the
states at each time would be:
    1: attacked
    2: in poison state
    3: in poison state
    4: attacked, poison duration resets to 3
    5: in poison state
    6: in poison state
    7: in poison state
    8: in normal state
This means that the total time that Ashe is in a poisoned condition is 5.
'''
# def find_poisoned_duration(time_series, duration):
#     pass
# Example Usage:
# time_series = [1, 4, 9]
# damage = find_poisoned_duration(time_series, 3)
# print(damage)
# Example Output:
#     8
#endregion



#region Problem 6: Sum Unique Elements
'''
PROBLEM 6: Sum Unique Elements
Write a function sum_of_unique_elements() that takes in two lists of
integers, lst1 and lst2, as parameters and returns the sum of the elements
that are unique in lst1.
An element is unique if:
 - it appears exactly once in lst1
 - it does not appear in lst2
'''
# def sum_of_unique_elements(lst1, lst2):
#     pass
# Example Usage:
# lstA = [1, 2, 3, 4]
# lstB = [3, 4, 5, 6]
# lstC = [7, 7, 7, 7]
# sum1 = sum_of_unique_elements(lstA, lstB)
# print(sum1)
# sum2 = sum_of_unique_elements(lstC, lstB)
# print(sum2)
# Example Output:
#     3
#     0
#endregion



#endregion