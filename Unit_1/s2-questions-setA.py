#
#
#

def print_list(lst):
    for item in lst:
        print (item)
lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)

# --- 3 --- #
def doubled(lst):
    for item in lst:
        print(item * 2)
doubled([1,2,3])

# --- 4 --- #
def doubled_list(lst):
    newList = []
    for item in lst:
        item *= 2
        newList.append(item)
    print(newList)
doubled_list([1,2,3])

# --- 4 --- #
def flip_sign(lst):
    newList = []
    for item in lst:
        item *= -1
        newList.append(item)
    print(newList)
flip_sign([1,-2,-3,4])

# --- 5 --- #