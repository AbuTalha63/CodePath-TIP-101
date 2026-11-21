'''
Write a function sum_of_number_strings() that takes in a list of strings nums. 
Each string is a representations of integers. The function should return the sum 
of these strings as an integer.

def sum_of_number_strings(nums):
    
Example Usage:

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
Example Output: 60


UPI

Understand:
I/O: List(only strings) / Integer

Plan:
- loop through string
- int(x)
- return integer result

Implement
'''
def sum_of_number_strings(nums):
    result = 0
    for num in nums:
        result += int(num)
    return result

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

'''
Write a function remove_duplicates() that takes in a sorted list of integers 
nums as a parameter and removes all duplicates in the list. The function returns
the modified list.

def remove_duplicates(nums):
    
Example Input: nums = [1,1,1,2,3,4,4,5,6,6]
Example Output: no_dups = [1,2,3,4,5,6]

UPI
Understand
I/O: Sorted list/Modified list (new list)
 - edge cases: 
        empty list => resturn the same empty list
        no dupliactes => the same list
Plan
declare function
initialize the result list (no_dups)
for loop to interate throught the list (nums)
    if num in nums not in no_dups                <=== core logic

return no_dups list


Implement
'''
# def remove_duplicates(nums):
#     no_dups = []
#     for num in nums:
#         if num in no_dups:
#             pass
#         else:
#             no_dups.append(num)
        #      no_dups += num
#         return no_dups

# nums = [1,1,1,2,3,4,4,5,6,6]
# no_dups = remove_duplicates(nums)
# print(no_dups)
    





    
 
def remove_duplicates(nums):
    no_dups = []
    for num in nums:
        if num not in no_dups:
            no_dups += [num]
    return no_dups

nums = [1, 1, 1, 2, 3, 4, 4, 5, 6, 6]
no_dups = remove_duplicates(nums)
print(no_dups)
   
   
   
   
'''
Write a function reverse_only_letters() that takes in a string s as a parameter. 
The function reverses the order of the letters in the string and returns the new 
string. Non-letter characters should remain in their original positions.

def reverse_only_letters(s):
    pass
Example Usage:

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
Example Output: j-Ih-gfE-dCba

Understand:
-I/O: Single string/ single string (just reversed)
 - non-alphanumerics should stay in the exact same place as the OG string
 - caps stays same

Plan:
define function
init new string
 - edge case: no non-letters exist


Implement:
'''
def reverse_only_letters(s):
    reversed = ""
    for char in s:
        if char.isalpha():
            reversed += char
        else:
            

# double pointer method 
            
    
    
    
    
    