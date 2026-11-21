class Pokemon:
	def __init__(self, name, types):
		self.name = name
		self.types = types
		self.is_caught = False 
  
	def print_pokemon(self):
		print({
			"name": self.name,   
			"types": self.types, 
			"is_caught": self.is_caught 
		})
	def catch(self):
		self.is_caught = True

	def choose(self):
		if self.is_caught:
			print(self.name + "I choose you")
		else:
			print(self.name + "is wild catch them if you can!")

	def add_type(self, new_type):
		self.types.append(new_type)
  
	def __repr__(self): return self.name


def get_by_type(my_pokemon, pokemon_type):
	result = []
	for pokemon in my_pokemon:
		if pokemon_type in pokemon.types:
			result.append(pokemon)
	return result
    
# initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")