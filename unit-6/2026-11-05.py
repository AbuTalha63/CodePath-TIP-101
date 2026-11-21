# ============================================================================
#  CodePath TIP101 | Unit 6, Session 1 - Working with Linked Lists
#  Problem Set Version 1
# ============================================================================
#
#  UMPIRE:  Understand -> Match -> Plan -> Implement -> Review -> Evaluate
#
#  Problems:
#    1. Nested Constructors
#    2. Find Frequency
#    3. Remove Tail          (debugging)
#    4. Find the Middle      (slow & fast pointers)
#    5. Is Palindrome?       (two pointers)
#    6. Put it in Reverse    (in place)
#
# ============================================================================


# ----------------------------------------------------------------------------
#  SHARED SETUP - used by every problem below
# ----------------------------------------------------------------------------



# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# ============================================================================
#  PROBLEM 1: Nested Constructors
# ============================================================================
#  Add a line of code (outside of the class) to create the linked list
#  4 -> 3 -> 2 in a single assignment statement.
# ----------------------------------------------------------------------------
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
# node1 = Node(4)
# node2 = Node(3)
# node3 = Node(2) non single line verison of connecting them



# Your single assignment statement here:
node1 = Node(4, Node(3, Node(2)))

print_list(node1)    # Expected: 4 -> 3 -> 2


# ============================================================================
#  PROBLEM 2: Find Frequency
# ============================================================================
#  Given the head of a linked list and a value val, return the frequency
#  of val in the list.
#
#  Example:
#    Input List:  3 -> 1 -> 2 -> 1
#    Input:       head = 3, val = 1
#    Output:      2
#
#  UMPIRE notes:
#    Understand: Using the first value of the linked list and value return the frequency
#    Match: 
#    Plan: 
#        - create a counter variable
#       - create a current variable for head
#        - while loop?
 #       - check if equal to the value with a if statement
 #      - .next to move to next item of the list
#
#
#
#
#    Evaluate:    Time O(?)  |  Space O(?)
#                 Variables defined:
#                 Why:
# ----------------------------------------------------------------------------

def count_element(head, val):
    count = 0
    current = head

    while current:
        if current.value == val:    # make sure to use .value
            count+=1
        current = current.next
        
    return count


# Tests:

my_node = Node(2, Node(3, Node(2, Node(1))))
print(count_element(my_node, 2))

# ============================================================================
#  PROBLEM 3: Remove Tail  (debugging)
# ============================================================================
#  The code below attempts to remove the tail of a singly linked list,
#  but it has a bug!
#
#  Create your own test cases, then use print statements and the stack
#  trace to find and fix the bug so the function correctly removes the
#  tail of the list.
#
#  Example:
#    Input List:              1 -> 2 -> 3 -> 4
#    Input:                   head = 1
#    Expected Return Value:   1
#    Expected Result List:    1 -> 2 -> 3
#
#  Debug notes:
#    What's going wrong?
#    How did we find it?
#    The fix:
# ----------------------------------------------------------------------------

# I have a bug!
def remove_tail(head):
    if head is None:  # If the list is empty, return None
        return None
    if head.next is None:  # If there's only one node, removing it leaves the list empty
        return None

    # Start from the head and find the second-to-last node
    current = head
    while current.next.next:
        current = current.next
        

    current.next = None  # Remove the last node by setting second-to-last node to None
    return head


# Test cases:

my_node = Node(2, Node(3, Node(2, Node(1))))
print(count_element(my_node, 2))


# ============================================================================
#  PROBLEM 4: Find the Middle  (slow & fast pointers)
# ============================================================================
#  A variation of the two-pointer technique from Unit 4 is to have a slow
#  and a fast pointer that move at different rates.
#
#  Given the head of a linked list, use the slow-fast pointer technique to
#  find the middle node. If there are two middle nodes, return the SECOND
#  middle node.
#
#  Example:
#    Input List:              1 -> 2 -> 3
#    Input:                   head = 1
#    Expected Return Value:   2
#
#  UMPIRE notes:
#    Understand:
#    Match:
#    Plan:
#    Evaluate:    Time O(?)  |  Space O(?)
#                 Variables defined:
#                 Why:
# ----------------------------------------------------------------------------

def find_middle_element(head):
    pass


# Tests:



# ============================================================================
#  PROBLEM 5: Is Palindrome?  (two pointers)
# ============================================================================
#  Given the head of a singly linked list, return True if the values of the
#  linked list are palindromic and False otherwise.
#  Use the two-pointer technique in your solution.
#
#  Example:
#    Input List:  1 -> 2 -> 1
#    Input:       head = 1
#    Output:      True
#
#  UMPIRE notes:
#    Understand:
#    Match:
#    Plan:
#    Evaluate:    Time O(?)  |  Space O(?)
#                 Variables defined:
#                 Why:
# ----------------------------------------------------------------------------

def is_palindrome(head):
    pass


# Tests:



# ============================================================================
#  PROBLEM 6: Put it in Reverse  (in place)
# ============================================================================
#  Given the head of a singly linked list, reverse the list and return the
#  head of the reversed list. You must reverse the list IN PLACE.
#
#  Example:
#    Input List:              1 -> 2 -> 3 -> 4
#    Input:                   head = 1
#    Expected Return Value:   4
#    Expected Result List:    4 -> 3 -> 2 -> 1
#
#  UMPIRE notes:
#    Understand:
#    Match:
#    Plan:
#    Evaluate:    Time O(?)  |  Space O(?)
#                 Variables defined:
#                 Why:
# ----------------------------------------------------------------------------

def reverse(head):
    pass


# Tests: