
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
def get_evolutionary_line(starter_pokemon):
    result = []
    current = starter_pokemon
    while current:
        if starter_pokemon.evolution != None:
            result.append(starter_pokemon.name)
            current = starter_pokemon.evolution
    return result

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)
