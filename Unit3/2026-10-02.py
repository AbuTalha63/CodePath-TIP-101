# Question 1


'''
Understand:
 - Input :List of Strings
 - Output: Integer sum
 - Need to convert the list of strings to nums, then return their sum
 - 
 - input will always be string, but always nums
 

Plan:
 - create function, 1 parameter of lst
 - Iterate through all items in the lst
 - Type cast each of the items into a int
 - iterate through them once more and add them
 - assign to variable
 - return variable


Implement:
'''
def sum_of_number_strings(nums):
    Sum = 0
    for i in nums:
        Sum += int(i)
    return Sum

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)


# Question  2: Remove Duplicates
'''
Understand:
input = list of sorted integers , can have duplicates 
output : list of unique integers

Plan:

- iterate through each item , if current_item is same as previous_item then remove current_item, else move to next item
- return the modified list


Implement:
1 1 1 2
'''

def remove_duplicates(nums):
    prev = -1
    for cur_num in nums:
        if cur_num == prev:
            nums.remove(cur_num)
            print(f"removing : {cur_num}")
        prev = cur_num

    return nums


nums = [1,1,1,2,3,4,4,5,6,6,6,6,6,6,6]
print(remove_duplicates(nums))
nums = [1,2,3,4,5,6]
print(remove_duplicates(nums))
