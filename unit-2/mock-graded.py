# AI DISCLOSURE: This mock assessment was written with the help of AI
# (Claude, by Anthropic), modeled on the format of the CodePath TIP101
# Unit 2 Assessment (Fall 2026). It is practice material, not an official test.
# This file is the GRADED + CORRECTED version of my submission. Corrections
# and grading notes were written with the help of AI (Claude, by Anthropic).
#
# ============================================================================
# GRADE: 45/60 (75%) - PASS (passing is 30/60)
# TIME:  45 min / 90 min
# ============================================================================
#   Q1 Multiple Choice ........ 5/5    correct (B)
#   Q2 Multiple Choice ........ 5/5    correct (C)
#   Q3 Multiple Choice ........ 5/5    correct (D)
#   Q4 Multiple Choice ........ 5/5    correct (B)
#   Q5 Matching Keys ......... 20/20   8/8 hidden tests passed
#   Q6 Most Frequent .......... 5/20   2/8 hidden tests passed (1 by coincidence)
#
#   Real Unit 2 attempts for comparison: 15/60, 15/60, 10/60 (0/120 coding)
#
# TAKEAWAYS
#   - Strong: building/comparing dictionaries, MC reading, code that compiles.
#   - Weak:   frequency maps under pressure (counts.get(x, 0) + 1), and
#             returning the KEY with the highest value (best-so-far over .items()).
#   - Next:   re-write Most Frequent from a blank file, then redo Frequency
#             Equality, Element Frequency > N, and Find Unique the same way.
# ============================================================================
#
# RULES
#   - 90 minutes (the real time limit). Start a timer before scrolling down.
#   - No notes, cheatsheets, lesson doc, or AI. Python docs are off limits too.
#   - You MAY run your code as often as you like. That is allowed on HackerRank.
#   - Q1-4: write your answer letter in the ANSWER line. 5 points each.
#   - Q5-6: write code. 20 points each, graded on hidden test cases.
#   - Passing is 30/60.
#   - When done, send me the whole file and your total time.

#region Q1 (Multiple Choice, 5 pts)
'''
What is the value of scores after running the following code?

    scores = {'ana': 5, 'ben': 8}
    scores['ana'] = 7
    scores['cy'] = 2

A) {'ana': 5, 'ben': 8, 'cy': 2}
B) {'ana': 7, 'ben': 8, 'cy': 2}
C) {'ana': 12, 'ben': 8, 'cy': 2}
D) KeyError
'''
# ANSWER: B
# GRADE: 5/5 - Correct. d[key] = value overwrites an existing key and adds a new one.
#endregion

#region Q2 (Multiple Choice, 5 pts)
'''
What is the output of the following code?

    inventory = {'pens': 10, 'pads': 4}
    print(inventory.get('clips', 0))

A) None
B) KeyError
C) 0
D) 'clips'
'''
# ANSWER: C
# GRADE: 5/5 - Correct. .get() returns the default when the key is missing.
#endregion

#region Q3 (Multiple Choice, 5 pts)
'''
What is the output of the following code?

    def mystery(d):
        result = []
        for key, val in d.items():
            if val > 2:
                result.append(key)
        return result

    print(mystery({'a': 1, 'b': 3, 'c': 5, 'd': 2}))

A) [3, 5]
B) ['b', 'c', 'd']
C) {'b': 3, 'c': 5}
D) ['b', 'c']
'''
# ANSWER: D
# GRADE: 5/5 - Correct. Filters on the value, appends the key; 2 is not > 2.
#endregion

#region Q4 (Multiple Choice, 5 pts)
'''
The following function should return a dictionary mapping each character in
the string s to the number of times it appears.

    # Input: "hello"
    # Expected Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    def count_letters(s):
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
            return counts

However, it has a bug! Which option best describes the cause?

A) counts.get(ch, 0) raises a KeyError the first time a character is seen.
B) The return statement is indented inside the loop, so the function returns
   after the first character.
C) The function should loop over range(len(s)) instead of s.
D) counts is never initialized, causing a NameError.
'''
# ANSWER: B
# GRADE: 5/5 - Correct. A return inside the loop exits on the first pass.
#endregion

#region Q5 (Coding, 20 pts): Matching Keys
'''
Write a function matching_keys() that takes in two dictionaries d1 and d2 and
returns a list of every key that appears in BOTH dictionaries AND has the same
value in both. The keys should appear in the list in the same order they
appear in d1. If there are no such keys, return an empty list.

Example 1:
    Input:  d1 = {'a': 1, 'b': 2, 'c': 3}, d2 = {'a': 1, 'b': 5, 'd': 3}
    Output: ['a']

Example 2:
    Input:  d1 = {'x': 'red', 'y': 'blue'}, d2 = {'y': 'blue', 'x': 'red'}
    Output: ['x', 'y']

Example 3:
    Input:  d1 = {'k': 9}, d2 = {}
    Output: []
'''
#
# Complete the 'matching_keys' function below.
#
# The function is expected to return a LIST.
# The function accepts DICTIONARY d1 and DICTIONARY d2 as parameters.
#
'''
UPI
Understand:
 - I/O: 2 DICTS / 1 LIST of matching KEYS across both dicts No values returned (but the values would have to match ofc too)
 - they key-value pairs have to match 100%, but the order does not have to (like as in their order within their respoective dicts)
 - in the returned list, the keys should be in the order they appear based on d1 specefically
 - no matching return empty list (Maybe indicates for loop since otherwise it would be a None retunred???)

Plan:
 - create function
 - init list empty
 - for loop over key / values in d1:
 - if key / value pair in in d2, add to list (make sure it can check for outta order ones too tho)
 - outta loop: return list
Implement:
'''
# GRADE: 20/20 - 8/8 hidden tests passed.
#
# Hidden tests included: both examples above, empty d1, d2 = {}, same key with
# different value types (1 vs '1'), order taken from d1, a None value, and
# list values.
#
# What went right:
#   - "key in d2 and value == d2[key]" puts the membership check FIRST.
#     'and' stops as soon as the left side is False, so d2[key] never runs for
#     a missing key -> no KeyError. Swapping the order would crash on
#     matching_keys({'k': 9}, {}).
#   - Looping over d1 gives d1's order for free.
#
# Polish (not point-losing):
#   - "key in d2.keys()" -> "key in d2". 'in' on a dict already checks keys.
#   - UPI note: the empty list doesn't need special handling. The accumulator
#     pattern returns [] on its own when nothing ever matches.

# MY SUBMISSION (kept for reference):
# def matching_keys(d1, d2):
#     # Write your code here
#     ans = []
#     for key, value in d1.items():
#         if key in d2.keys() and value == d2[key]:
#             ans.append(key)
#     return ans

# CORRECTED / POLISHED:
def matching_keys(d1, d2):
    ans = []
    for key, value in d1.items():
        if key in d2 and value == d2[key]:
            ans.append(key)
    return ans


# Sample tests (the hidden tests include more)
print(matching_keys({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 5, 'd': 3}))   # ['a']
print(matching_keys({'x': 'red', 'y': 'blue'}, {'y': 'blue', 'x': 'red'}))  # ['x', 'y']
print(matching_keys({'k': 9}, {}))                                          # []
#endregion

#region Q6 (Coding, 20 pts): Most Frequent
'''
Write a function most_frequent() that takes in a list of integers nums and
returns the integer that appears the most times. You may assume there is
exactly one most frequent value (no ties). If nums is empty, return None.

Example 1:
    Input:  [3, 1, 3, 2, 3, 1]
    Output: 3

Example 2:
    Input:  [7]
    Output: 7

Example 3:
    Input:  []
    Output: None
UPI:
Understand:
 - I/O: list / int
 - no ties
 - None if empty
Plan:
 - function
 - init empty dict
 - for each num in list nums, create corresponding dict entry
  - new dict [key = num instance variable] += 1 (?)
 - return highest value - not sure yet
Implement:
'''
#
# Complete the 'most_frequent' function below.
#
# The function is expected to return an INTEGER (or None).
# The function accepts INTEGER_ARRAY nums as parameter.
#
# GRADE: 5/20 - 2/8 hidden tests passed.
#   PASS []           -> None  (empty guard worked)
#   PASS [1, 1, 2]    -> 1     (coincidence: function always returns 1)
#   FAIL [3,1,3,2,3,1] -> 1, expected 3
#   FAIL [7]          -> 1, expected 7
#   FAIL [5, 5, 2]    -> 1, expected 5
#   FAIL [-4,-4,0,-4] -> 1, expected -4
#   FAIL [2,9,9,9,2,0] -> 1, expected 9
#   FAIL [0, 0, 1]    -> 1, expected 0
#
# The plan had the right shape (frequency map, then find the highest).
# Each half had one bug:
#
# BUG 1: d1[num] = 1 RESETS the count instead of adding to it.
#   Every time 3 appears, its count goes back to 1.
#   The "+= 1 (?)" instinct in the Plan was right, but d[num] += 1 raises
#   KeyError on a key that doesn't exist yet (same lesson as Restock).
#   Fix: the frequency map line ->  counts[num] = counts.get(num, 0) + 1
#
# BUG 2: max(d1.values()) returns the highest COUNT, not the NUMBER.
#   The question asks WHICH number appears most, i.e. the KEY with the
#   biggest value. Fix: best-so-far tracking over the dict (Best Book pattern).
#
# Lesson: a submission that compiles and runs still earns points, even a
# wrong one. Never leave a body blank.

# MY SUBMISSION (kept for reference):
# def most_frequent(nums):
#     # Write your code here
#     if not nums: return
#     d1 = {}
#     for num in nums:
#         d1[num] = 1
#     return max(d1.values())

# CORRECTED:
def most_frequent(nums):
    if not nums:
        return None

    # 1. Build the frequency map
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # 2. Find the KEY with the highest count (best-so-far)
    best = nums[0]
    for num, count in counts.items():
        if count > counts[best]:
            best = num
    return best


# Sample tests (the hidden tests include more)
print(most_frequent([3, 1, 3, 2, 3, 1]))   # 3
print(most_frequent([7]))                  # 7
print(most_frequent([]))                   # None
#endregion