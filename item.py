class Item:
	
	"""
	I'll now change the item code to work for instance of item / weapon / armor
	instead of strings.
	"""
	
	def __init__(self, name, weight, description, type, cursed = False):
		self.name = name
		self.weight = weight
		self.description = description
		self.type = type
		self.cursed = cursed
		
	def get_name(self):
		return self.name
		
	def describe_item(self):
		return self.description
		
class Weapon(Item):
		
		def __init__(self, name, weight, description, type, mod, cursed = False, stat = 'damage'):
			super().__init__(name, weight, description, type, cursed)
			self.stat = stat
			self.mod = mod
			
class Armor(Item):
		
		def __init__(self, name, weight, description, type, mod, cursed = False, stat = 'defense'):
			super().__init__(name, weight, description, type, cursed)
			self.stat = stat
			self.mod = mod

class Consumable(Item):
		
		def __init__(self, name, weight, description, type, mod, cursed = False, stat = 'current_health'):
			super().__init__(name, weight, description, type, cursed)
			self.stat = stat
			self.mod = mod
			
class Lightsource(Item):
	
	def __init__(self, name, weight, description, type, burn_length, cursed = False, lit = False):
			super().__init__(name, weight, description, type, cursed)
			self.lit = lit
			self.burn_length = burn_length
			
	def light(self):
		"""
		Sets the lit flag to true.
		"""
		if self.burn_length > 0:	
			self.lit = True	
		else:
			print("There is nothing left to burn.")
		
	def snuff(self):
		"""
		Set the lit flag to false. 
		"""
		self.lit = False
					
	def burn(self):
		"""
		If the lit flag is true, the method will subtract one from the burn length every turn.
		If the burn length reaches 0, it will set the lit flag to false. 
		The Lightsource lit flag will be used to change the current room lit flag. 
		"""
		if self.lit == True:
			self.burn_length -= 1
			if self.burn_length == 0:
				self.snuff()
				print("The flame dwindles and dies.")
			
	
class Spellbook(Item):
	
	"""
	Takes in a spell.spell() method and will add this to the player's spellbook when interacted with.'
	"""
	
	def __init__(self, name, weight, description, type, spell, cursed = False):
			super().__init__(name, weight, description, type, cursed)
			self.spell = spell
			
	def add_spell(self):
			return name, spell
			
											
		
			
	
	
	
	
	


		