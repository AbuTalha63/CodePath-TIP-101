# AI DISCLOSURE: The problems in this file were formatted and/or written with
# the help of AI (Claude, by Anthropic). Problems 1-3 are restatements of the
# coding questions from the CodePath TIP101 Unit 5 Assessment (Version A,
# Fall 2026). Problems 4-7 are additional practice problems.

#region Problem 1: Get Grandchildren (from Unit 5 Assessment)
'''
PROBLEM 1: Get Grandchildren

The Person class below defines a person with a last name, first name, and a
list of children. Each child in the list of children is an instance of Person.
The method add_child() adds a child to a person's list of children.

Add a method to the Person class called get_grandchildren() that returns a
list of the person's grandchildren.

Additional test cases to check yourself against:
    - A person with one child who has four children returns all four, in order.
    - A person with two children, only one of whom has children, returns just
      that one's children.
    - Calling get_grandchildren() must not modify any person's children list.
'''
class Person:
    def __init__(self, first, last):
        self.last_name = last
        self.first_name = first
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        
    # Write your code here        
    def get_grandchildren(self):
        result = []
        # grandchild = self.children[0].children
        # return grandchild
        for child in self.children:
            result += child.children
        return result
    
    def print_person(self):
        print({
            "first name": self.first_name,   
            "last name": self.last_name 
        })
        

# Example Usage 1:
johndoe = Person("John", "Doe")
janedoe = Person("Jane", "Doe")
jimmydoe = Person("Jimmy", "Doe")
johndoe.add_child(janedoe)
janedoe.add_child(jimmydoe)
johndoe.get_grandchildren()

# printing must be looped
grandkids = johndoe.get_grandchildren()   # store the returned list
for person in grandkids:                  # each item is a Person object
    person.print_person()                 # call the method on that object

# john doe
#    |
# jane doe
#     |
# jimmy doe

# Example Output 1:
#     [jimmydoe] DONE

# Example Usage 2:
johndoe = Person("John", "Doe")
janedoe = Person("Jane", "Doe")
johndoe.add_child(janedoe)
grandkids = johndoe.get_grandchildren()
for person in grandkids:
    person.print_person()


# Example Output 2:
#     [] DONE



#endregion





#region Problem 2: Extend Linked List (from Unit 5 Assessment)
'''
PROBLEM 2: Extend Linked List

Given the tail of a linked list and a list of values, write a function that
adds each element in values as a node with value values[i] to the end of the
linked list. The nodes added to the linked list should maintain the same order
as the elements in values. The function does not need to return anything.



Additional test cases to check yourself against:
    - values is an empty list: the linked list is unchanged.
    - values has exactly one element.
'''
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

def extend_linked_list(tail, values):
    # Write your code here
    for value in values:
        new_node = Node(value)
        tail.next = new_node
        tail = new_node

# Example Input:
    # linked list = a->b->c
tail = c, values = ['d', 'e', 'f']

# Example Output:
# a->b->c->d->e->f

#endregion



#region Problem 3: Copy First N Nodes (from Unit 5 Assessment)
'''
PROBLEM 3: Copy First N Nodes

Given the head of a linked list and a positive integer n, create a new linked
list that copies the first n nodes of the original linked list. Return the head
of the new list.

If n is greater than or equal to the length of the original list, the function
should copy the entire list. If the list contains no nodes, return None.

The copy must use new Node objects. Re-using the original nodes is not a copy.

Additional test cases to check yourself against:
    - head is None: return None.
    - n is larger than the length of the list: the whole list is copied.
    - The original list is unchanged after the call.

Understand:
 - I/O: 
'''
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node
        
    def print_node(self):
        print({
            "Node: ": self,
            "value: ": self.value,
            "next_node: ": self.next
        })

def copy_first_n_nodes(head, n):
    pass
                    

# Example Input:
#     head = node1, n = 3
#    linked list = a->b->c->d->e
# Example Output:
#     a->b->c

node_5 = Node("e")
node_4 = Node("d", node_5)
node_3 = Node("c", node_4)
node_2 = Node("b", node_3)
node_1 = Node("a", node_2)
#endregion




#region Problem 4: Skip-Level Reports
'''
PROBLEM 4: Skip-Level Reports

An Employee has a name and a list of direct reports. Each report in the list is
an instance of Employee. The method add_report() adds a direct report to an
employee's list of reports.

Add a method to the Employee class called get_skip_reports() that returns a
list of the employee's skip-level reports, meaning the direct reports of each
of this employee's direct reports.

class Employee:
    def __init__(self, name):
        self.name = name
        self.reports = []

    def add_report(self, report):
        self.reports.append(report)

    # Write your code here

Example Usage:
    ada = Employee("Ada")
    grace = Employee("Grace")
    alan = Employee("Alan")
    katherine = Employee("Katherine")
    linus = Employee("Linus")

    ada.add_report(grace)
    ada.add_report(alan)
    grace.add_report(katherine)
    alan.add_report(linus)

    skips = ada.get_skip_reports()
    for employee in skips:
        print(employee.name)

Example Output:
    Katherine
    Linus

Additional test cases to check yourself against:
    - An employee with reports who have no reports of their own returns [].
    - An employee with no reports at all returns [].
    - Calling get_skip_reports() must not modify any employee's reports list.
'''
#endregion


#region Problem 5: Build Linked List
'''
PROBLEM 5: Build Linked List

Write a function build_linked_list() that takes in a Python list of values and
returns the head of a linked list containing those values in the same order.

Use a loop. Do not create the nodes one line at a time by hand.

If the input list is empty, return None.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def build_linked_list(values):
    # Write your code here

def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    print(" -> ".join(result))

Example Usage:
    head = build_linked_list(["Mario", "Luigi", "Wario", "Toad"])
    print_linked_list(head)

Example Output:
    Mario -> Luigi -> Wario -> Toad

Additional test cases to check yourself against:
    - An empty list returns None.
    - A list with one value returns a single node whose next is None.
'''
#endregion




#region Problem 6: Copy Linked List
'''
PROBLEM 6: Copy Linked List

Write a function copy_linked_list() that takes in the head of a linked list and
returns the head of a brand-new linked list with the same values in the same
order.

Every node in the returned list must be a new Node object. If the original list
is empty, return None.


Additional test cases to check yourself against:
    - head is None: return None.
    - Changing a value in the copy does not change the original.
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def copy_linked_list(head):
    # Write your code here
    if not head:
        return None
    current = head
    new_head = current.value
    while current.next is not None:
        current_value = current.value
        new_node_tail = Node(current_value)
        new_node_tail.next = current.next
    return new_head               # BUGGY CODE - not final just a work in progress playing around / logic etc

# node creation
node_3 = Node("c")
node_2 = Node("b", node_3)
node_1 = Node("a", node_2)
    
# Example Usage:
#     # original linked list: a->b->c
#     copy = copy_linked_list(a)
#     print(copy.value)
#     print(copy.next.value)
#     print(copy is a)
#     print(copy.next is a.next)

# Example Output:
#     a
#     b
#     False
#     False
    

#endregion




#region Problem 7: Values Until
'''
PROBLEM 7: Values Until

Write a function values_until() that takes in the head of a linked list and a
value stop_value. The function should return a Python list of the values in the
linked list, starting at the head and stopping as soon as it reaches a node
whose value equals stop_value. The stop_value itself is not included.

If no node has the value stop_value, return the values of the entire list.
If the list is empty, return an empty list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def values_until(head, stop_value):
    # Write your code here

Example Usage:
    # linked list: a->b->c->d->e
    print(values_until(a, "d"))
    print(values_until(a, "z"))
    print(values_until(a, "a"))

Example Output:
    ['a', 'b', 'c']
    ['a', 'b', 'c', 'd', 'e']
    []

Additional test cases to check yourself against:
    - head is None: return [].
    - stop_value is the value of the last node.
'''
#endregion