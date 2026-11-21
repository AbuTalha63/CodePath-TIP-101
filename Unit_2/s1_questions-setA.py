'''
1. Understand
    - input lists
    - output booleas
    - comparing list a to list b, if every elemnt in a is in b then true, if not false

2. Plan
- define function
- declare lists
- for loop, for each in a if in b, return true, else false


3. Implement
'''
def all_in(a, b):
    for num in a:
        if num not in b:
            return False
    return True
        
lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))

'''

'''
