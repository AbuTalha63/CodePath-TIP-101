'''

Unit 3 - Session 2



Problem 1:
Write a function sum_of_number_strings() that takes in a list of strings nums. 
Each string is a representations of integers. The function should return the sum 
of these strings as an integer.

    
Example Usage:

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
Example Output: 60



UPI 

Understand 
I/O: List of strings / Int
- Always guranteed to be ints
- 

Plan 

Define function
initilize variable for return
iterate list w/ for loop & cast it to integer
add to variable
return
 
 
 Test cases:
Implement
'''
def sum_of_number_strings(nums):
    sum = 0
    for num in nums:
        sum += int(num)
    return sum
    
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

#Problem 2

'''

'''



