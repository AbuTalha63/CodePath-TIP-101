#region ---------- UNIT 1 SESSION 1 PROBLEM SET VERSION 1 ---------- #

# AI DISCLOSURE: The problems in this file were formatted with the help of
# AI (Claude, by Anthropic). The problems come from CodePath TIP101
# (Unit 1, Session 1).

#region Problem 1: Hello World!
'''
PROBLEM 1: Hello World!

Given the following lines of code, work with your group members to place the
lines in order and write and call your first Python function!

'''
def hello_world():
    print("Hello world!")

hello_world()
#endregion


#region Problem 2: Today's Mood
'''
PROBLEM 2: Today's Mood

The following function uses a variable, mood, to print out "Today's mood: 😎".
Copy this code into your IDE and update the mood variable to print out your
mood for today.

'''

def todays_mood():
    mood = "🍪"
    print("Today's mood: " + mood)

todays_mood()

#endregion

#region Problem 3: Lunch Menu
'''
PROBLEM 3: Lunch Menu

The following function accepts one parameter menu. Copy this code into your
IDE and add a function call so that "Lunch today is: 🍕" is printed to the
console.
'''
def print_menu(menu):
    print("Lunch today is: " + menu)
    
print_menu("🍪")

#endregion

#region Problem 4: Sum of Two Integers
'''
PROBLEM 4: Sum of Two Integers

The following function returns the sum of two integers: a and b.

def sum(a, b):
    return a + b

Use the sum() function to calculate the sum of 13 and 27. Then, use the sum()
function again to double the calculated sum and print the result to the
console.

Note: Do not use any mathematical operators such as +, -, *, or / when
solving this problem.

Example Input: 20 and 8
Example Output: 56
'''
#endregion

#region Problem 5: Product of Two Integers
'''
PROBLEM 5: Product of Two Integers

Write a function product() that returns the product of two integers, a and b.

Example Input: 22 and 7
Example Result: 154
'''
#endregion

#region Problem 6: Classify Age
'''
PROBLEM 6: Classify Age

Write a function classify_age() that takes an integer age as a parameter and
returns "child" if the age is less than 18, and returns "adult" otherwise.

Example Usage:
    output = classify_age(18)
    print(output)
    output = classify_age(7)
    print(output)
    output = classify_age(50)
    print(output)

Output:
    adult
    child
    adult
'''
#endregion

#region Problem 7: What time is it?
'''
PROBLEM 7: What time is it?

Let's put what we learned in Problems 1-4 all together! Write a function
named what_time_is_it() that takes an integer hour as a parameter.

If hour is 2, the function should return "taco time 🌮".
If hour is 12, the function should return "peanut butter jelly time 🥪".
Otherwise, the function should return "nap time 😴".

Example Usage:
    time = what_time_is_it(2)
    print(time)
    time = what_time_is_it(7)
    print(time)
    time = what_time_is_it(12)
    print(time)

Output:
    taco time 🌮
    nap time 😴
    peanut butter jelly time 🥪
'''
#endregion

#region Problem 8: Blackjack
'''
PROBLEM 8: Blackjack

In the game Blackjack, players try to draw a hand of cards that totals as
close to 21 as possible. Players "bust" if their cards total more than 21.
Players say "Hit me!" if they want the dealer to give them another card.

Write a function called blackjack() that takes an integer score as a
parameter.

If score equals 21, print "Blackjack!".
If score is greater than 21, print "Bust!".
If score is greater than or equal to 17 and less than 21, print "Nice hand!".
If score is less than 17, print "Hit me!".

Example Usage:
    blackjack(21)
    blackjack(24)
    blackjack(19)
    blackjack(10)

Output:
    Blackjack!
    Bust!
    Nice hand!
    Hit me!
'''
#endregion

#region Problem 9: First Item
'''
PROBLEM 9: First Item

Write a function get_first() that takes in a list as a parameter and returns
the first item in the list. Return None if the list is empty.

def get_first(lst):
    pass

Example Input: [3,1,6,7,5]
Example Output: 3
'''
#endregion

#region Problem 10: Last Item
'''
PROBLEM 10: Last Item

Write a function get_last() that takes in a list as a parameter and returns
the last item in the list. Return None if the list is empty.

def get_last(lst):
    pass

Example Input: [3,1,6,7,5]
Example Output: 5
'''
#endregion

#region Problem 11: Counter
'''
PROBLEM 11: Counter

Write a function counter() that uses the range function to print numbers
between 1 and a given stop value (inclusive).

def counter(stop):
    pass

Example Usage:
    counter(7)

Example Output:
    1
    2
    3
    4
    5
    6
    7
'''
#endregion

#region Problem 12: Sum of 1 to 10
'''
PROBLEM 12: Sum of 1 to 10

Write a function sum_ten() that returns the sum of numbers from 1 to 10.

def sum_ten():
    pass

Example Usage:
    output = sum_ten()

Example Result:
    output = 55
'''
#endregion

#region Problem 13: Total Sum
'''
PROBLEM 13: Total Sum

Write a function sum_positive_range() that returns the sum of numbers from 1
to a given stop value (inclusive).

def sum_positive_range(stop):
    pass

Example Usage:
    sum = sum_positive_range(6)

Example Result:
    sum = 21
'''
#endregion

#region Problem 14: Total Sum in Range
'''
PROBLEM 14: Total Sum in Range

Write a function sum_range() that returns the sum of numbers from a given
start value to a given stop value (inclusive).

def sum_range(start, stop):
    pass

Example Usage:
    sum = sum_range(3, 9)

Example Result:
    sum = 42
'''
#endregion

#region Problem 15: Negative Numbers
'''
PROBLEM 15: Negative Numbers

Write a function print_negatives() that takes a list of integers lst and
prints all negative numbers in the list.

def print_negatives(lst):
    pass

Example Usage:
    print_negatives([3,-2,2,1,-5])

Example Output:
    -2
    -5

Example Usage:
    print_negatives([1,2,3,4,5])

Example Output:
    None
'''
#endregion

#endregion

#region ---------- UNIT 1 CHEATSHEET ---------- #
'''
UNIT 1 CHEATSHEET

In-Scope: may appear on the assessment
Not In-Scope: useful, but not required

Unit Goals
  - Write, use, and modify variables, functions, and print statements
  - Use conditional logic (if statements)
  - Work with lists (accessing, iterating, etc)

------------------------------------------------------------
BUILT-IN FUNCTIONS
------------------------------------------------------------

print(s)
Prints the message s to the console.

    print("Welcome to TIP101!")      # Prints Welcome to TIP101!
    print(100)                       # Prints 100

    s = "Welcome to CodePath!"
    num = 7
    print(s)                         # Prints Welcome to CodePath!
    print(num)                       # Prints 7

    lst = ["TIP101", "TIP102", "TIP103"]
    print(lst)                       # Prints ['TIP101', 'TIP102', 'TIP103']

    x = 5
    y = 3
    print(x + y)                     # Prints 8

    def my_func():
        return 6

    result = my_func()
    print(result)                    # Prints 6
    print(my_func())                 # Prints 6 (same as above)

len(s)
Returns the length of a list or string. Accepts one parameter s.

    lst = ['a', 'b', 'c']
    print(len(lst))                  # 3

    s = 'abcd'
    print(len(s))                    # 4

range(start, stop, step)
Returns a sequence of numbers.
  - start: first number (optional, defaults to 0)
  - stop: last value, EXCLUSIVE (required)
  - step: increment (optional, defaults to 1)

    range(10)          # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    range(1, 11)       # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    range(0, 30, 5)    # 0, 5, 10, 15, 20, 25

------------------------------------------------------------
CONDITIONALS
------------------------------------------------------------
Defined with if, elif, and else. The body runs if the expression after
if / elif evaluates to True.

    x = 3
    if x > 1:
        print("This line will execute!")
    if x > 5:
        print("This line will not execute!")

    x = 10
    y = 20
    if x > y:
        print("x is greater than y")
    elif y > x:
        print("y is greater than x")       # this runs

    x = 20
    y = 20
    if x > y:
        print("x is greater than y")
    elif y > x:
        print("y is greater than x")
    else:
        print("x and y are equal")          # this runs

------------------------------------------------------------
FOR LOOPS
------------------------------------------------------------
for num in nums: iterates through every item in a sequence (list, string,
range). Useful for accessing each element or repeating code.

    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)                 # each fruit on a new line

    for i in range(5):
        print(i)                     # 0 to 4

------------------------------------------------------------
LIST METHODS & SYNTAX
------------------------------------------------------------

lst.append(item)
Adds an item to the end of the list.

    lst = [1, 2, 3, 4]
    lst.append(5)
    print(lst)                       # [1, 2, 3, 4, 5]

lst.sort()
Sorts the list in ascending order. No required parameters, returns nothing.

    lst = [4, 2, 1, 3]
    lst.sort()
    print(lst)                       # [1, 2, 3, 4]

    lst = ['b', 'a', 'd', 'c']
    lst.sort()
    print(lst)                       # ['a', 'b', 'c', 'd']

List Indexing: lst[index]
  - Zero-based: the first element is at index 0
  - Positive indices count from the start, negative from the end (-1 is last)
  - An index that does not exist causes an IndexError

    fruits = ["apple", "banana", "cherry"]
    print(fruits[0])                 # apple
    print(fruits[2])                 # cherry
    print(fruits[-1])                # cherry
    print(fruits[-2])                # banana
    # print(fruits[3])               # IndexError: list index out of range

List Slicing: lst[start:end]
Returns a NEW list from index start up to (not including) end.
  - start defaults to the beginning, end defaults to the end
  - Negative indices count from the end
  - The original list is not modified

    nums = [0, 1, 2, 3, 4, 5]
    print(nums[1:4])                 # [1, 2, 3]
    print(nums[:3])                  # [0, 1, 2]
    print(nums[3:])                  # [3, 4, 5]
    print(nums[-3:])                 # [3, 4, 5]

------------------------------------------------------------
BONUS CONCEPTS (Not In-Scope)
------------------------------------------------------------
lst.insert(x, item)   Inserts item into list at index x
lst.remove(item)      Removes item from list
lst.pop(x)            Removes element at index x from list
lst.copy()            Creates a copy of a list
abs(x)                Returns the absolute value of a number x
enumerate()           Returns indices and values of a list as pairs
'''
#endregion