#region ---------- UNIT 3 SESSION 2 PROBLEM SET VERSION 2 ---------- #
# AI DISCLOSURE: The problems in this file were formatted with the help of
# AI (Claude, by Anthropic). The problems come from CodePath TIP101
# (Unit 3, Session 2).


#region Problem 1: String to Integer
'''
PROBLEM 1: String to Integer
Write a function string_to_integer_mapping() that takes in a string of
digits s as a parameter and returns a list where each element is the integer
value of the corresponding digit in the string.
'''
# def string_to_integer_mapping(s):
#     pass
# Example Usage:
# s = "12345"
# print(string_to_integer_mapping(s))
# Example Output:
#     [1, 2, 3, 4, 5]
#endregion



#region Problem 2: Delete Minimum
'''
PROBLEM 2: Delete Minimum
Write a function delete_minimum_elements() that takes in a list of integers
nums as a parameter and continuously removes the minimum element until the
list is empty. The function returns a new list of all the elements in nums in
the order in which they were removed.
'''
# def delete_minimum_elements(nums):
#     pass
# Example Usage:
# nums = [5, 3, 2, 8, 3, 1]
# removed_lst = delete_minimum_elements(nums)
# print(removed_lst)
# Example Output:
#     [1, 2, 3, 3, 5, 8]
#endregion



#region Problem 3: Longest Common Prefix
'''
PROBLEM 3: Longest Common Prefix
Write a function longest_common_prefix() that takes in a list of strings
strings as a parameter. The function returns the longest common prefix (not
substring) of all strings, and if there is none, it returns an empty string
"".
'''
# def longest_common_prefix(strings):
#     pass
# Example Usage:
# strings = ["flower", "flow", "flight"]
# common_string = longest_common_prefix(strings)
# print(common_string)
# strs = ["dog", "racecar", "car"]
# common_str = longest_common_prefix(strs)
# print(common_str)
# Example Output:
#     fl
#     (empty line - the second call returns "")
#endregion



#region Problem 4: Consecutive Characters
'''
PROBLEM 4: Consecutive Characters
Write a function count_consecutive_characters() that takes in a string str1
as a parameter and returns the count of the most frequent consecutive
character.
'''
# def count_consecutive_characters(str1):
#     pass
# Example Usage:
# str1 = "aaabbcaaaa"
# count = count_consecutive_characters(str1)
# print(count)
# str2 = "abcde"
# count2 = count_consecutive_characters(str2)
# print(count2)
# Example Output:
#     4
#     1
#endregion



#region Problem 5: Partition Labels
'''
PROBLEM 5: Partition Labels
Write a function partition_label() that takes in a string s as a parameter.
s consists of lowercase letters and represents the order of characters as
they appear in a document. The function partitions s into as many parts as
possible so that each unique letter appears in at most one part, and returns
a list of integers representing the size of these parts.
'''
# def partition_label(s):
#     pass
# Example Usage:
# s1 = "ababcbacadefegdehijhklij"
# print(partition_label(s1))
# s2 = "abcabcbadefffeda"
# print(partition_label(s2))
# Example Output:
#     [9, 7, 8]
#     (s1 partitioned into "ababcbaca", "defegde" and "hijhklij")
#     [16]
#     (s2 cannot be partitioned into more parts because of the "a" at the end)
#endregion



#region Problem 6: Interleave Lists
'''
PROBLEM 6: Interleave Lists
Write a function interleave_lists() that accepts two lists as parameters.
The function should return a new list that combines the given lists by
alternating which list it takes its next element from. It will take elements
in order, and if one list is longer it will append the remaining elements to
the end of the interleaved list.
'''
# def interleave_lists(lst1, lst2):
#     pass
# Example Usage:
# lst1 = [1, 2, 3, 4]
# lst2 = [10, 20]
# inter_lst = interleave_lists(lst1, lst2)
# print(inter_lst)
# Example Output:
#     [1, 10, 2, 20, 3, 4]
#endregion



#endregion