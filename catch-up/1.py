def classify_age(age):
    if age >= 18:
        return 'Adult'
    else:
        return 'child'
    
print(classify_age(18))   # adult
print(classify_age(7))    # child
print(classify_age(50))   # adult

def sum_range(start, stop):
    total = 0
    for num in range(start, stop + 1):
        total += num
    return total
    
print(sum_range(3, 9))   # 42
print(sum_range(1, 10))  # 55

def print_pair(dictionary, target):
    if target in dictionary:
        print(f"Key: {target}\nValue: {dictionary[target]}")
    else:
        print('That pair does not exist!')

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")    # Key: patrick / Value: star
print_pair(dictionary, "plankton")   # That pair does not exist!
print_pair(dictionary, "spongebob")  # Key: spongebob / Value: squarepants


def keys_v_values(dictionary):
    
    k_list = dictionary.keys()
    v_list = dictionary.values()
    k_sum = sum(k_list)
    v_sum = sum(v_list)
    
    if k_sum > v_sum:
        return 'keys'
    elif v_sum > k_sum:
        return 'values'
    else:
        return 'balanced!'


dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print(keys_v_values(dictionary1))  # values

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
print(keys_v_values(dictionary2))  # keys

def restock_inventory(current_inventory, restock_list):
    for item in restock_list:
        if item in current_inventory:
            current_inventory.values() += item
        else:
            




current_inventory = {"apples": 30, "bananas": 15, "oranges": 10}
restock_list = {"oranges": 20, "apples": 10, "pears": 5}
print(restock_inventory(current_inventory, restock_list))
# {"apples": 40, "bananas": 15, "oranges": 30, "pears": 5}


'''

Write a function all_in() that takes in a list of integers a and a list of integers b as parameters. Given these two lists, return True if every element in list a is in list b. Return False otherwise.

def all_in(a, b):
    pass
Example Usage:

lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))
Example Output:

True
False

'''
