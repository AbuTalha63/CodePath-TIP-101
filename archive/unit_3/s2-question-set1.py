'''
Question 1;
Write a function cast_vote() that records a vote for a candidate in an election.
The function accepts a dictionary votes that maps candidates to their current number
of votes and a string candidate that represents the candidate the user would like to vote
for. If the candidate doesn't exist, add them to the dictionary. The function should return
the updated dictionary.

def cast_vote(votes, candidate):
    votes{}
    for i in range votes:
        if i isnot candidate 

print(votes[])
    

Example Usage:

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)

Example Output:

{'Alice': 6, 'Bob': 3}
{'Alice': 6, 'Bob': 3, 'Gina': 1}


Understand
    Input - Votes dictionary and String Candidate
    Output -  Updated dictionary
    Edge Cases - empty dictionary, empty string
    Example - 

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)

{'Alice': 6, 'Bob': 3}
{'Alice': 6, 'Bob': 3, 'Gina': 1}

Plan

1. Define the function cast vote with parameters(votes, candidate).
2. if candidate not in votes
      votes[candidate] = 1
   else:
      votes[candidate] +=1
3.  return votes

Implement
'''

def cast_vote(votes, candidate):
    if candidate in votes:
       votes[candidate] += 1
    else:
       votes[candidate] = 1
    return votes

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
cast_vote(votes, "Gina")
cast_vote(votes, "Mamdani")
cast_vote(votes, "Mamdani")
cast_vote(votes, "Mamdani")
cast_vote(votes, "Mamdani")
cast_vote(votes, "Mamdani")
cast_vote(votes, "Mamdani")
cast_vote(votes, "Mamdani")
print(votes)


""""
Question 2;
Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys 
common to both dictionaries. The function returns a list of common keys.

def common_keys(dict1, dict2):
	pass

Example Usage:
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

Example Output:
['b', 'c']
Understand:



Plan:

1. Create a funciton coommon keys with two dictionaries passed in
2. Create an empty list called common_list
3. Create a outer for loop to loop to through the keys of dictoionary a
4. Create an inner for loop to loop through 


Implement:


"""""





