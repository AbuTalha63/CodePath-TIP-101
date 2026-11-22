#region ---------- UNIT 5 SESSION 1 PROBLEM SET VERSION 1 ---------- #

class Pokemon:
    def __init__(self, name, types, evolution=None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution


    def catch(self):
        self.is_caught = True

    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")
            
    def add_type(self, new_type):
        self.types.append(new_type)
        
    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })
        
my_pokemon = Pokemon("Pikachu", "Electric")

squirtle = Pokemon("Squirtle", "Water")
squirtle.print_pokemon()

squirtle.is_caught = True
squirtle.print_pokemon()

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()

# Problem 7: Get Pokemon - function to get all Pokemon Instance that have given type via args
def get_by_type(my_pokemon, pokemon_type):
    result_types = []
    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            result_types.append(pokemon.name)
    return result_types

jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)

# problem 8: function to return evoloutionary line for the Pokemon class
# def get_evolutionary_line(starter_pokemon):
#     result = []
#     current = starter_pokemon
#     while current:
#         # if starter_pokemon.evolution != None:
#             result.append(starter_pokemon.name)
#             current = starter_pokemon.evolution
#     return result

def get_evolutionary_line(starter_pokemon):
    result = []
    current = starter_pokemon
    while current:
        result.append(current.name)
        current = current.evolution
    return result

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

# # 8 test cases
charmander_list = get_evolutionary_line(charmander)
print(charmander_list)
charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)
charizard_list = get_evolutionary_line(charizard)
print(charizard_list)
# supposed to be:
# [`Charmander`, `Charmeleon`, `Charizard`]
# [`Charmeleon`, `Charizard`]
# ['Charizard']     DONE

# 9: Node class

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
  
# make 2 instances / objects of node class with value(s) of a & b
node_two = Node("b")
node_one = Node("a")

# test cases
print(node_one.value)
print(node_one.next)
print(node_two.value)
print(node_two.next)

# 10: Linking Nodes
node_two = Node("b")
node_one = Node("a", node_two) # re instatiated the object to ensure print does not error for prev test cases

print(node_one.value)
print(node_one.next.value)
print(node_two.value)

# 11: Mario party
class MarioNode:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
# Create the list ["Mario", "Luigi", "Wario", "Toad"] as a linked list

node_4 = MarioNode("Toad")
node_3 = MarioNode("Wario", node_4)
node_2 = MarioNode("Luigi", node_3)
node_1 = MarioNode("Mario", node_2)

# test cases
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

# Problem 12: Printing Linked List

node_five = Node("e")
node_four = Node("d", node_five)
node_three = Node("c", node_four)
node_two = Node("b", node_three)
node_one = Node("a", node_two)       # re instantiated these to test this question + not have issues with earlier objects prior

def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

parts = print_linked_list(node_one)
print(" -> ".join(parts))
#endregion