#region ---------- UNIT 3 SESSION 1 PROBLEM SET VERSION 2 ---------- #

# AI DISCLOSURE: The problems in this file were formatted with the help of
# AI (Claude, by Anthropic). The problems come from CodePath TIP101
# (Unit 3, Session 1).

#region Problem 1: Perfect Match
'''
PROBLEM 1: Perfect Match

Copy and paste the following function:

def match_made(dictionary):
    for key, value in dictionary.items():
        print(f"{key} and {value} are a perfect match.")

Add code to your IDE so that your program prints out the following to the
console:

Peanut butter and Jelly are a perfect match.
Spongebob and Patrick are a perfect match.
Ash and Pikachu are a perfect match.
'''
def match_made(dictionary):
    for key, value in dictionary.items():
        print(f"{key} and {value} are a perfect match.")


# Example Usage:
# Add your code here:

# Example Output:
#     Peanut butter and Jelly are a perfect match.
#     Spongebob and Patrick are a perfect match.
#     Ash and Pikachu are a perfect match.
#endregion

#region Problem 2: Remove Char
'''
PROBLEM 2: Remove Char

Write a function remove_char() that takes in a string s and an integer n as
parameters. The function returns a new string with the nth character removed
where 0 < n < len(s).
'''
def remove_char(s, n):
    pass


# Example Usage:
s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)

# Example Output:
#     typo
#endregion

#region Problem 3: Count Vowels
'''
PROBLEM 3: Count Vowels

Write a function vowel_count() that takes in a string s as a parameter and
returns the number of vowels in the given string.
'''
def vowel_count(s):
    pass


# Example Usage:
my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)

# Example Output:
#     3
#     10
#     0
#endregion

#region Problem 4: Reverse Sentence
'''
PROBLEM 4: Reverse Sentence

Write a function reverse_sentence() that takes in a string sentence as a
parameter and returns the string with the order of the words reversed. The
sentence will only contain alphabetic characters and spaces to separate the
words. If there is only one word in the sentence, the function returns the
original string.
'''
def reverse_sentence(sentence):
    pass


# Example Usage:
sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))

# Example Output:
#     good no to up am I swear solemnly I
#endregion

#region Problem 5: String Compression
'''
PROBLEM 5: String Compression

Write a function compress_string() that takes in a string my_str as a
parameter and performs basic string compression using counts of repeated
characters.

For example, the string "aabcccccaaa" would become "a2b1c5a3". If the
compressed string does not become smaller than the original string, return
the original string. Assume the string only has alphabetic characters.
'''
def compress_string(my_str):
    pass


# Example Usage:
my_str = "aaaaabbcccd"
compressed_str = compress_string(my_str)
print(compressed_str)

my_str2 = "abcde"
compressed_str2 = compress_string(my_str2)
print(compressed_str2)

# Example Output:
#     a5b2c3d1
#     abcde
#     (my_str2 is not converted because "a1b1c1d1e1" is double the length)
#endregion

#region Problem 6: Needle in a Haystack
'''
PROBLEM 6: Needle in a Haystack

Write a function find_the_needle() that takes in two string parameters: a
needle and a haystack. The function returns the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.
'''
def find_the_needle(haystack, needle):
    pass


# Example Usage:
haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))

# Example Output:
#     2
#     -1
#endregion

#endregion
