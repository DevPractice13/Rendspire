class Spell:
	"""
	Superclass for all spells. Individual effects will be added in subs.
	Maybe have cool downs instead of mana? 
	
	Need to find a way to add these to the player's dict from an item. 
	Could test add to a dict before main loop. '
	
	Currently testing keeping spells as part of the player class. '
	"""
	
	def __init__(self):
		pass
		
	def describe_spell(self):
		print(description)
		
	def display_items(self, dict ={}):
	   	"""Display items with numbered choices.
	   	Uses the instance name. 
	   	
	   	"""
	   	for i, (item_name, item_obj) in enumerate(dict.items(), start=1):
	   	   print(f"{i} - {item_obj.name}")
		
	
	   	
	def get_choice(self, choices, input_text):
	   	
	   while True:
	       choice = input(f"{input_text}")
	       if choice.isdigit():
	           choice = int(choice)
	           if 1 <= choice <= len(inven):
	               # Return the item corresponding to the number
	               return list(choices.keys())[choice - 1]
	           else:
	           	print("Invalid choice. Please enter a number from the list or 'e' to exit.")
	           	
	       elif choice == 'e':
	       	break
	       else:
	               
	       	print("Invalid choice. Please enter a number from the list or 'e' to exit.")
		
	def remove_curse(self, spellbook = {}):
		curse_list = [item for item in spellbook if item.cursed == True]
		self.display_items(curse_list)
		self.get_choice(curse_list)
		
		
		
		

		
		
				
		
		