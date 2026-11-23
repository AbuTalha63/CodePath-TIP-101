#region ---------- UNIT 3 SESSION 1 PROBLEM SET VERSION 1 ---------- #

# AI DISCLOSURE: The problems in this file were formatted with the help of
# AI (Claude, by Anthropic). The problems come from CodePath TIP101
# (Unit 3, Session 1).

#region Problem 1: Calling Mississippi
'''
PROBLEM 1: Calling Mississippi

Copy and paste the following function:

def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")

Call the function so that it prints out the following to the console (without
calling the function more than once):

    1 mississippi
    2 mississippi
    3 mississippi
    4 mississippi
    5 mississippi
'''
#endregion

#region Problem 2: Swap Ends
'''
PROBLEM 2: Swap Ends

Write a function swap_ends() that accepts a string my_str as a parameter and
returns a new string where the first and last characters from my_str are
swapped.

def swap_ends(my_str):
    pass

Example Usage:
    my_str = "boat"
    swapped = swap_ends(my_str)
    print(swapped)

Example Output:
    toab
'''
#endregion

#region Problem 3: Is Pangram
'''
PROBLEM 3: Is Pangram

Write a function is_pangram() that takes in a string my_str as a parameter and
returns True if the string is a pangram and False if not. A pangram is a
sentence containing every letter in the English alphabet.

def is_pangram(my_str):
    pass

Example Usage:
    my_str = "The quick brown fox jumps over the lazy dog"
    print(is_pangram(my_str))

    str2 = "The dog jumped"
    print(is_pangram(str2))

Example Output:
    True
    False
'''
#endregion

#region Problem 4: Reverse String
'''
PROBLEM 4: Reverse String

Write a function reverse_string() that takes a string my_str as a parameter
and returns the string reversed.

def reverse_string(my_str):
    pass

Example Usage:
    my_str = "live"
    print(reverse_string(my_str))

Example Output:
    evil
'''
#endregion

#region Problem 5: First Unique
'''
PROBLEM 5: First Unique

Write a function first_unique_char() that, given a string my_str as a
parameter, finds the first non-repeating character in it and returns its
index. If it does not exist, then return -1.

def first_unique_char(my_str):
    pass

Example Usage:
    my_str = "leetcode"
    print(first_unique_char(my_str))

    str2 = "loveleetcode"
    print(first_unique_char(str2))

    str3 = "aabb"
    print(first_unique_char(str3))

Example Output:
    0
    2
    -1
'''
#endregion

#region Problem 6: Minimum Distance
'''
PROBLEM 6: Minimum Distance

Write a function min_distance() that takes in a list of strings words and two
strings word1 and word2 as parameters. The function should return the minimum
distance between word1 and word2 in the list of words. The distance between
one word and an adjacent word in the list is 1.

def min_distance(words, word1, word2):
    pass

Example Usage:
    words = ["the", "quick", "brown", "fox", "jumped", "the"]
    dist1 = min_distance(words, "quick", "jumped")
    dist2 = min_distance(words, "the", "jumped")
    print(dist1)
    print(dist2)

    words2 = ["code", "path", "code", "contribute",  "practice"]
    dist3 = min_distance(words2, "code", "practice")
    print(dist3)

Example Output:
    3
    1
    2
'''
#endregion

#endregion

#region ---------- UNIT 3 CHEATSHEET ---------- #
'''
UNIT 3 CHEATSHEET

In-Scope: may appear on the assessment
Not In-Scope: useful, but not required

Unit Goals
  - Insert variables and Python expressions into strings
  - Index and access subsections of a string
  - Loop over strings
  - Solve problems involving strings, lists, dictionaries, or a combination
    of the three

------------------------------------------------------------
STRING METHODS & SYNTAX
------------------------------------------------------------

s.lower()
Returns s as a lowercase string. Accepts no parameters.

    s = 'Hello World!'
    print(s.lower())     # 'hello world!'

    s = 'HELLO WORLD'
    print(s.lower())     # 'hello world'

s.split(separator)
Splits the string into a list along whitespace or the specified separator.
  - separator: the characters to split along (optional). By default, splits
    along any whitespace.
  - Returns a list of the substrings of s.

    s = 'Never gonna give you up'
    print(s.split())     # ['Never', 'gonna', 'give', 'you', 'up']

    s = 'Never-gonna-let-you-down'
    print(s.split("-"))  # ['Never', 'gonna', 'let', 'you', 'down']

s.join(x)
Turns an iterable x into a string using s as the separator between elements.
  - s is the separator placed between items
  - x: the iterable whose items will be joined (required)
  - Returns a string of the items in x separated by s

    lst = ['Never', 'gonna', 'run', 'around', 'and', 'desert', 'you']
    print(' '.join(lst))   # 'Never gonna run around and desert you'

    lst = ['Never', 'gonna', 'make', 'you', 'cry']
    print('-'.join(lst))   # 'Never-gonna-make-you-cry'

s.strip(characters)
Removes whitespace or specified characters from either end of the string.
  - characters: the characters/substring to remove from either end (optional).
    If not specified, whitespace is removed.
  - Returns the string with whitespace or characters removed.

    s = '       Never gonna say goodbye       '
    print(s.strip())       # 'Never gonna say goodbye'

    s = '????Never gonna tell a lie and hurt you?????'
    print(s.strip('?'))    # 'Never gonna tell a lie and hurt you'

------------------------------------------------------------
TUPLES
------------------------------------------------------------
A tuple stores multiple items in a single variable. Usually used to group 2-3
items (3 items is sometimes called a "triple"). Commonly used to store pairs
of data together or return multiple values from a function.

Tuples are defined using round brackets.

    my_tuple = ("Mario", "Luigi")
    print(my_tuple)        # ("Mario", "Luigi")

Like lists and strings, tuples can be indexed.

    my_tuple = ("Mario", "Luigi")
    mario = my_tuple[0]
    luigi = my_tuple[1]
    print(mario)           # "Mario"
    print(luigi)           # "Luigi"

Like strings, tuples are immutable: their contents cannot be updated.
Updating a tuple means creating a new tuple.

    my_tuple = (10, 20)
    my_tuple[0] = 30       # TypeError: 'tuple' object does not support item assignment

------------------------------------------------------------
BUILT-IN FUNCTIONS
------------------------------------------------------------

round(number, decimal)
Returns a number rounded to the specified decimal.
  - number: the number to round (required)
  - decimal: number of decimals to include (optional, defaults to 0 which
    rounds to the nearest integer)

    x = 3.14159
    print(round(x, 2))     # 3.14
    print(round(x))        # 3

enumerate(x)
Takes an iterable (list, dictionary, string) and adds a counter. Often used
to loop over the indices and values of an iterable at the same time.
  - x: an iterable (required)
  - start: the value to start the counter at (optional, defaults to 0)
  - Returns a sequence of numbers coupled with values from the iterable

    my_string = 'code'
    for index, char in enumerate(my_string):
        print(index, char)
    # 0 c
    # 1 o
    # 2 d
    # 3 e

    cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']
    for count, cereal in enumerate(cereals, start=1):
        print(count, cereal)
    # 1 cheerios
    # 2 fruity pebbles
    # 3 cocoa puffs

zip(x, y)
Takes two or more iterables and returns a sequence of tuples. The first item
from each iterable forms the first tuple, the second item from each forms the
second tuple, and so on, until the shortest iterable runs out. Useful for
iterating over multiple iterables in parallel or combining data from separate
iterables.
  - Accepts two or more iterables
  - Returns tuples pairing x[i] with y[i] where 0 <= i < min(len(x), len(y))

    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    print(list(zip(names, ages)))
    # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

    names = ['Alice', 'Bob', 'Charlie', 'David']
    ages = [25, 30, 35]
    print(list(zip(names, ages)))
    # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

------------------------------------------------------------
COMPARING STRINGS AND LISTS
------------------------------------------------------------

Similarities
  - Ordered sequences: both are ordered sequences of data
  - Indexed by integers: lst[0] or s[0]
  - Sliceable: lst[1:3] or s[1:3]
  - Iterable: both can be looped over with a for loop
  - Length: len() works on both

Differences
  - Content type: strings are an ordered sequence of characters. Lists are an
    ordered sequence of elements of any type (integers, strings, other lists).
  - Mutability:
      Strings are immutable. To update a string, create a new string.
          s = 'Try'
          s[0] = 'C'    # TypeError: 'str' object does not support item assignment
      Lists are mutable. You can update a list without creating a new one.
          lst = ['T', 'r', 'y']
          lst[0] = 'C'
          print(lst)    # ['C', 'r', 'y']

------------------------------------------------------------
BONUS CONCEPTS (Not In-Scope)
------------------------------------------------------------
s.isalpha()   True if all characters in the string are alphabetic letters
s.isalnum()   True if all characters are alphanumeric (a-z or 0-9)
s.find(x)     Start index of the first occurrence of substring x, or -1 if
              x is not in the string
s.count(x)    Frequency of the substring x in the string
Sets          Data type that groups multiple pieces of data. Unordered,
              unchangeable, and cannot contain duplicates.
'''
#endregion