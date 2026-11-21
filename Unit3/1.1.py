# Unit 3 session 1 problem set 1

# Question 1

def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")
        
count_mississippi(6)

# Question 2
def swap_ends(my_str):
    first_letter = my_str[0]
    last_letter = my_str[-1] # negative indexing to shortcut to the last character
    first_letter, last_letter = last_letter, first_letter
    middle_word = my_str[1:-1]
    swapped_str = first_letter + middle_word + last_letter
    return swapped_str
    

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)


# Question 3
def is_pangram(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
          
my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))


# Question 4
def reverse_string(my_str):
    for char in my_str:
        