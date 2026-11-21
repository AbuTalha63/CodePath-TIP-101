#Tuesday 6/2/2026
#Problem set version 1
#question 1
def hello_world():
    print("Hello world!")
    
hello_world()

#question 2
def todays_mood():
    mood = "😎"
    mood = "excited"
    print("Today's mood: " + mood)

todays_mood()

#question 3
def print_menu(menu):
    print("Lunch today is: " + menu)
    
print_menu("🍕")


#question 4
def sum(a, b):
    return a + b
a = sum(13, 27)
b = sum(13, 27)
c = a + b                       # maybe this OR
print(sum(20, 8) + sum(20, 8))  # maybe this - both work

#5
def product(a, b):
    product = a * b
    print(product)
    
product(22, 7)

#6
def classify_age(age):
    if (age >= 18):
        return "adult"
    elif (age < 18 and age > 0):
        return "child"
    else:
        return "invalid age"
ageResult = classify_age(12) #child
print(ageResult)
ageResult = classify_age(18) #adult
print(ageResult)
ageResult = classify_age(-3) #invlaid
print(ageResult)

# 7
def what_time_is_it(hour):
    if hour == 2:
        return "taco time"
    elif hour == 12:
        return "peanut butter jelly time 🥪"
    else:
        return "nap time"
time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)


""" q 8
In the game Blackjack, players try to draw a hand of cards that totals as close to 21 as
possible. Players "bust" if their cards total more than 21. Players say "Hit me!" if they want the dealer to give them another card.

Write a function called blackjack() that takes an integer score as a parameter.
If score equals 21, print "Blackjack!".
If score is greater than 21, print "Bust!".
If score is greater than or equal to 17 and less than 21, print "Nice hand!".
If score is less than 17, print "Hit me!".
"""
def blackJack(cards):
    if cards == 21:
        return "Blackjack"
    elif cards > 21:
        return "Bust!"
    elif cards >= 17 and cards < 21:
        return "Nice Hand"
    elif cards < 17:
        return "Hit Me!"
a = blackJack(30)
print(a)
b = blackJack(3)
print(b)
c = blackJack(17)
print(c)
d = blackJack(21)
print(d)

#9
def get_first(lst):
    if (len(lst) != 0):
        return lst[0]
    else:
        return None
print(get_first([3, 6, 2, 0, 1]))
print(get_first([]))

#10
def get_last(lst):
    if (len(lst) != 0):
        x = len(lst)
        return lst[x-1]
    else:
        return None

print(get_last([3,1,6,7,5,90,78]))
print(get_last([]))


# --- 11 --- #
"""
Understand
only input is stop value (+ 1 since its inclusive and the range function is exclusive)
one parameter: stop
edge cases: negative numbers, 0
we count up from 1 not 0

Plan  (corrected via Claude)
the range function already counts for you within the given range
the only thing left to do is print the varibale

Implement
"""
def counter(stop):
    for x in range(1, stop+1):
        print(x)

counter(7)


# --- 12 --- #
"""
Understand

Plan

Implement
"""
def sum_ten():
    num = 0
    for x in range (1, 11): #11 since the stop value is exclusive
        num += x
    return num
    
print(sum_ten())


# --- 13 --- #
def sum_positive_range(stop):
    num = 0
    for x in range(1, stop+1):
        num += x
    return num

print(sum_positive_range(6))
print(sum_positive_range(10))

# --- 14 --- #
def sum_range(start, stop):
    num = 0
    for x in range(start, stop+1):
        num += x
    return num

print(sum_range(3, 9))
print(sum_range(1, 10))

# --- 15 --- #
def print_negatives(lst):
    newList = []
    for num in lst:
        if (num < 0):
            newList.append(num) #does not return None as per prompt requirements, how come??? figure out
    return newList

lst = [1, 2, -6, 99, -90]
print(print_negatives(lst))
lst = [1,2,3,4,5,0]        #does not return None as per prompt requirements, how come??? figure out
print(print_negatives(lst))

# --- 15 - take 2(get it to show None) --- #
def print_negatives_2(lst):
    newList = []
    for x in lst:
        if (lst[x] < 0 ):
            newList.append(x)
        return newList
lst = [1, 2, -6, 99, -90]
print(print_negatives(lst))
lst = [1,2,3,4,5,0]        #does not return None as per prompt requirements, how come??? figure out
print(print_negatives(lst))

def print_negs(list):
    for num in list:
        if (num < 0):
            print(num) #MISTAKE: all you needed was a print statment versus the return statement you were using
        
usman = [1,2,3,4,5,0]
print(print_negs(usman))

cookie = [-90, -92, -56, 22, 90]
print_negs(cookie)


# --- END PROBLEM SET VERSION 1 --- #