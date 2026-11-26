#region ---------- UNIT 3 SESSION 1 PROBLEM SET VERSION 1 ---------- #

# AI DISCLOSURE: The problems in this file were formatted with the help of
# AI (Claude, by Anthropic). The problems come from CodePath TIP101
# (Unit 3, Session 1).

#region Unit 3 Cheatsheet
'''
UNIT 3 CHEATSHEET (Strings and Lists)
You are still expected to know required material from earlier units.

UNIT GOALS
 - Insert variables and Python expressions into strings
 - Index and access subsections of a string
 - Loop over strings
 - Solve problems involving strings, lists, dictionaries, or a combination

---------------------------------------------------------------------------
IN-SCOPE: STRING METHODS
---------------------------------------------------------------------------
s.lower()            -> returns s in lowercase. No parameters.
                        'Hello World!'.lower()        # 'hello world!'

s.split(separator)   -> returns a LIST of substrings. Separator is optional;
                        default splits on any whitespace.
                        'Never gonna give'.split()    # ['Never', 'gonna', 'give']
                        'a-b-c'.split('-')            # ['a', 'b', 'c']

s.join(x)            -> turns iterable x into ONE string, with s placed
                        between items. x is required.
                        ' '.join(['run', 'around'])   # 'run around'
                        '-'.join(['make', 'you'])     # 'make-you'

s.strip(characters)  -> removes whitespace (default) or the given characters
                        from BOTH ends only.
                        '   hi   '.strip()            # 'hi'
                        '??hi??'.strip('?')           # 'hi'

---------------------------------------------------------------------------
IN-SCOPE: TUPLES
---------------------------------------------------------------------------
 - Store multiple items in one variable; usually 2-3 items (3 = a "triple").
 - Used to group pairs of data or return multiple values from a function.
 - Defined with round brackets, indexed like lists and strings.
 - IMMUTABLE, like strings.
        my_tuple = ("Mario", "Luigi")
        my_tuple[0]          # 'Mario'
        my_tuple[0] = "Wario"  # TypeError: 'tuple' object does not support
                               # item assignment

---------------------------------------------------------------------------
IN-SCOPE: BUILT-IN FUNCTIONS
---------------------------------------------------------------------------
round(number, decimal) -> decimal is optional, defaults to 0 (nearest int).
                          round(3.14159, 2)   # 3.14
                          round(3.14159)      # 3

enumerate(x, start)    -> pairs a counter with each item of x. start is
                          optional, defaults to 0.
                          for index, char in enumerate('code'):
                              print(index, char)   # 0 c / 1 o / 2 d / 3 e

zip(x, y, ...)         -> sequence of tuples pairing x[i] with y[i].
                          STOPS AT THE SHORTEST iterable.
                          list(zip(['Al', 'Bo'], [25, 30]))
                          # [('Al', 25), ('Bo', 30)]

---------------------------------------------------------------------------
STRINGS vs LISTS
---------------------------------------------------------------------------
SIMILAR:  both are ordered, indexed by integers (s[0], lst[0]), sliceable
          (s[1:3]), iterable (for loops), and work with len().

DIFFERENT:
 - Content:    strings hold only characters; lists hold anything.
 - Mutability: strings are IMMUTABLE -> build a new string to change one.
                   s = 'Try'
                   s[0] = 'C'        # TypeError
               lists are MUTABLE.
                   lst = ['T', 'r', 'y']
                   lst[0] = 'C'      # ['C', 'r', 'y']

---------------------------------------------------------------------------
NOT IN-SCOPE (bonus, not on the assessment)
---------------------------------------------------------------------------
s.isalpha()  -> True if all characters are letters (a-z)
s.isalnum()  -> True if all characters are letters or digits
s.find(x)    -> start index of first occurrence of x, or -1 if absent
s.count(x)   -> number of times substring x appears
Sets         -> unordered, unchangeable, no duplicates
'''
#endregion

#region Problem 1: Calling Mississippi
'''
PROBLEM 1: Calling Mississippi
Copy and paste the following function:
def count_mississippi(limit):
    for num in range(1, limit):
        print(f"{num} mississippi")
Call the function so that it prints out the following to the console
(without calling the function more than once):
1 mississippi
2 mississippi
3 mississippi
4 mississippi
5 mississippi
'''
def count_mississippi(limit):
    for num in range(1, limit):
        print(f"{num} mississippi")
# Call the function here:
count_mississippi(6)
#endregion

#region Problem 2: Swap Ends
'''
PROBLEM 2: Swap Ends

Write a function swap_ends() that accepts a string my_str as a parameter and
returns a new string where the first and last characters from my_str are
swapped.
'''
def swap_ends(my_str):
    first = my_str[0]
    middle = my_str[1:len(my_str) - 1]
    last = my_str[len(my_str) - 1]
    return last + middle + first


# Example Usage:
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)

# Example Output:
#     toab
#endregion

#region Problem 3: Is Pangram
'''
PROBLEM 3: Is Pangram

Write a function is_pangram() that takes in a string my_str as a parameter
and returns True if the string is a pangram and False if not. A pangram is a
sentence containing every letter in the English alphabet.
'''
# def is_pangram(my_str):
    # for char in my_str:
        


# Example Usage:
# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))

# Example Output:
#     True
#     False
#endregion

#region Problem 4: Reverse String
'''
PROBLEM 4: Reverse String

Write a function reverse_string() that takes a string my_str as a parameter
and returns the string reversed.
'''
# def reverse_string(my_str):
    # pass


# # Example Usage:
# my_str = "live"
# print(reverse_string(my_str))

# Example Output:
#     evil
#endregion

#region Problem 5: First Unique
'''
PROBLEM 5: First Unique

Write a function first_unique_char() that given a string my_str as a
parameter, finds the first non-repeating character in it and returns its
index. If it does not exist, return -1.
'''
# def first_unique_char(my_str):
#     pass


# # Example Usage:
# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))

# Example Output:
#     0
#     2
#     -1
#endregion

#region Problem 6: Minimum Distance
'''
PROBLEM 6: Minimum Distance

Write a function min_distance() that takes in a list of strings words and two
strings word1 and word2 as parameters. The function should return the minimum
distance between word1 and word2 in the list of words. The distance between
one word and an adjacent word in the list is 1.
'''
# def min_distance(words, word1, word2):
#     pass


# # Example Usage:
# words = ["the", "quick", "brown", "fox", "jumped", "the"]
# dist1 = min_distance(words, "quick", "jumped")
# dist2 = min_distance(words, "the", "jumped")
# print(dist1)
# print(dist2)

# words2 = ["code", "path", "code", "contribute", "practice"]
# dist3 = min_distance(words2, "code", "practice")
# print(dist3)

# Example Output:
#     3
#     1
#     2
#endregion

#endregion
