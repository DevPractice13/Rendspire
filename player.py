class Player:
	
	def __init__(self, current_room, area_2_room, inventory = {}, max_weight = 10, current_weight = 0, equipped = {}, light = {},
							max_health = 10, current_health = 10, attack = 10, defense = 5, speed = 2, damage = 5, special_turn_count = 0,
							counting = False, ran = False, spells=["Remove Curse"]):
		self.spells = spells
		
		#the room instance the player is in. 
		self.current_room =  current_room
		#area 2's first room
		self.area_2_room = area_2_room
		
		#special turn counter for keeping track of lit Lightsources
		self.special_turn_count = special_turn_count
		#flag for counting something, just light right now
		self.counting = counting
		#dict for the Lightsource instances
		self.light = light
		#run away flag
		self.ran = ran
		
		#max and current total weight of items. 
		self.max_weight = max_weight
		self.current_weight = current_weight
		self.equipped = equipped
		
		#modifier for temporary defense
		self.def_mod = 2
		
		#flags
		self.defending = False
		self.is_alive = True
		
		#stats
		self.max_health = max_health
		self.current_health = current_health
		self.attack = attack
		self.defense = defense
		self.speed = speed
		self.damage = damage 
		
		#list of player's items.
		self.inventory = inventory
		
	
	
	def show_stats(self):
			"""
			Prints max health over current health. 
			"""
			
			print(f"HP: {self.max_health}/{self.current_health}")
			
	def snuff_out(self, a = False, b = False):
		if self.light:
			
			print("You snuff out the light.")
			self.special_turn_count = 0
			self.counting = False
			new_item = self.light.pop("Candle", None)
			self.inventory["Candle"] = new_item
			
		else:
			print("You have nothing to snuff out.")
			
	def show_spell_book(self):
		self.get_item_choice(self.spells)
	
	def read_spell_book(self):
		pass
		
		
	def unequip(self):
		"""
		If there is a weapon in the equipped dictionary and if the chosen item from the list
		is in the equipped, then remove the item from the equipped and assign it to inventory with '= new_item'.
		"""
		
		if self.equipped:
			equip_command = self.get_item_choice(self.equipped)
				
			if equip_command in self.equipped:
				   new_item = self.equipped[equip_command]
				   
				   	
				   if new_item is not None:
				   	
				   	
				   	if new_item.cursed is False:
				   		if new_item.type == "lightsource":
				   			print("You snuff out the light.")
				   			self.special_turn_count = 0
				   			self.counting = False
				   			new_item = self.light.pop(equip_command, None)
				   			self.inventory[equip_command] = new_item
				   		
				   		else:
				   			
				   			new_item = self.equipped.pop(equip_command, None)
				   			self.inventory[equip_command] = new_item
				   			self.stat_modify(new_item.stat, new_item.mod, False)
				   			print(f"You unequip a {new_item.get_name()}")
				   	
				   	else:
				   		print("You can't unequip that. It's cursed!")
				   else:
				   	print("You can't unequip that.")
		else:
			   print("You have nothing to unequip.")
		
	
	
			
	def stat_modify(self, stat, modifier, add):
		"""
		Updates stats from items. 
		"""
		
		if add:
			
			max_check = self.current_health + modifier
		
			if stat == "current_health":
				if max_check <= self.max_health:
				    self.current_health += modifier
				    print(f"You have increased your health by {modifier} to {self.current_health}.")
				    
				else:
					print("Your health is already full!")
					
		
			if stat == "damage":
				self.damage += modifier
				print(f"You have increased your damage by {modifier} to {self.damage}.")
			
			if stat == "defense":
				self.defense += modifier
				print(f"You have increased your defense by {modifier} to {self.defense}.")
		
		else:
			if stat == "current_health":
				self.max_health -= modifier
				print(f"You have decreased your health by {modifier} to {self.current_health}.")
		
			if stat == "damage":
				self.attack -= modifier
				print(f"You have decreased your damage by {modifier} to {self.attack}.")
			
			if stat == "defense":
				self.defense -= modifier
				print(f"You have decreased your defense by {modifier} to {self.defense}.")
	
	def defend(self, a = True, b = True):
			"""
			Adds the defense modifier when the defense combat option is chosen.
			A and B are unused. 
			"""
			
			self.defending = True
			self.stat_modify("defense", self.def_mod, True)
			
			
	def undefend(self):
	        """
	        Removes the defending modifier. 
	        """
	        
	        if self.defending:
	            self.stat_modify("defense", self.def_mod, False)
	            
	        self.defending = False
	        
	def interact(self):
		
		
		if self.current_room.is_lit:
			if self.current_room.story_beat:
				
				print(f"Would you like to interact with the {self.current_room.story_name}? y/n")
				command = input(">")
				if command == 'y':
					#make a list of interactables here
					self.current_room.play_story()
			else:
				print("There's nothing here to interact with.")
				
		else:
			print("You can't' see anything!")
	
	def equip(self, a = True, b = True):
		
		if self.inventory:
		
			equip_command = self.get_item_choice(self.inventory)
			
			if equip_command in self.inventory:
			    
			    #Can the dict class call go directly into check_weight?
			    #player must enter the key exactly. Is there a way to use numbers? 
			    new_item = self.inventory[equip_command]
			    #check_1 = self.check_weight(new_item.weight)
			    
			    #if check_1:
			    	
			    if new_item is not None:
			    	if new_item.type == "weapon" or new_item.type == "armor":
			    		
			    		print(f"You equip a {new_item.get_name()}")
			    		new_item = self.inventory.pop(equip_command, None)
			    		self.equipped[equip_command] = new_item
			    		self.stat_modify(new_item.stat, new_item.mod, True)
			    		
			    	elif new_item.type == "consumable":
			    		print(f"You quaff a {new_item.get_name()}")
			    		self.stat_modify(new_item.stat, new_item.mod, True)
			    		self.inventory.pop(equip_command, None)
			    		
			    	elif new_item.type == "spellbook":
			    		new_spell = new_item.add_spell()
			    		self.spells.append(new_spell)
			    		
			    	elif new_item.type == "lightsource":
			    		if not self.light:
			    			print(f"You light a {new_item.get_name()}. It has {new_item.burn_length} turns left until it dies.")
			    			new_item = self.inventory.pop(equip_command, None)
			    			self.light[equip_command] = new_item
			    			#How do we get the turn count in here? 
			    			new_item.light()
			    			#Set the counting flag to true, this will trigger a count in the main loop every turn. 
			    			self.counting = True
			    			
			    			self.current_room.is_lit = True
			    		else:
			    			print("You already have a lightsource!")
			    		
			    	else:
			    		print("You can't equip that.")
			    else:
			    	print("You can't equip that.")
		
		else:
			print("You have nothing to equip.")
			
	def show_light(self):
		"""
		Reminder that you're using a candle. 
		"""
		if len(self.light) == 1:
			print("Your candle casts a faint glow.")
			
	def update_candle(self):
		if len(self.light) == 1:
			self.light['Candle'].burn()
			if self.light['Candle'].lit is False:
				del self.light['Candle']
			
	def use_key(self):
		#What about multiple keys?
		"""
		Idea: Have the use key method check for any key that starts with Key.
		We can then use unique key name for every item but still have this
		method register a real key instance. 
		"""
		if True in self.current_room.locked_list.values():
			#changed from "key"
			
			for key in self.inventory:
				if key.startswith("Key"):
					print("What door do you want to unlock?")
					door_choice = input('>')
					valid = self.current_room.locked_list
					if door_choice in valid:
						del self.current_room.locked_list[door_choice]
						print("You unlock the door.\nThe key crumbles to dust!")
						del self.inventory[key]
						break
					else:
						print("There is no locked door in that direction.")
						break
					
				else:
					print("That is not a valid command.")
			else:
				print("You don't have any keys.")
		else:
			print("There are no locked doors.")
			
	def teleport(self):
			"""
			Jump to a room. Currently only used to transport to second area after boss fight. 
			"""
			self.current_room = self.area_2_room
			self.current_room.describe_room()
			
		
	def move(self, direction):
		"""
		Move accepts the direction command and changes the current room
		to the next room if there is a connected room in that direction. 
		"""
		if direction not in self.current_room.locked_list:
			if direction in self.current_room.connection_list:
			 	
			 		
		  		#print("You can go that way")
		  		self.current_room = self.current_room.connection_list[direction]
		  		if self.light:
		  			self.current_room.is_lit = True
		  		self.current_room.describe_room()
			else:
		 		print("You can't go that way.")
		else:
		 	print("The door is locked.")
		
	def show_current_room(self):
		self.current_room.describe_room()
	
	def show_inventory(self):
		
		if self.inventory:
			print("You have the following items in your inventory:")
			"""
			for i in self.inventory:
				print(i)
			"""
			self.display_items(self.inventory)
		else:
			print("Empty!")
	
	def show_equipment(self):
			
			if self.equipped:
				print("You have the following items equipped:")
				"""
				for i in self.equipped:
					print(i)
				"""
				self.display_items(self.equipped)
			else:
				print("You feel bare.")
			
	def check_weight(self, item_weight):
		weight_test = item_weight + self.current_weight
		if weight_test < self.max_weight:
			print("You can lift that easy! \n")
			self.current_weight += item_weight
			return True
		else:
			return False
	
	def display_items(self, dict):
	   	"""Display items with numbered choices.
	   	Uses the instance name. 
	   	
	   	"""
	   	for i, (item_name, item_obj) in enumerate(dict.items(), start=1):
	   	   print(f"{i} - {item_obj.name}")
	
	def get_item_choice(self, inven):
	   """Get the player's choice of item by number."""
	   if self.current_room.is_lit:
	   	
	   	self.display_items(inven)
	   else:
	   	print("There's something down there but you can't tell what it is...")
	   while True:
	       choice = input("Choose an item by number: ")
	       if choice.isdigit():
	           choice = int(choice)
	           if 1 <= choice <= len(inven):
	               # Return the item corresponding to the number
	               return list(inven.keys())[choice - 1]
	           else:
	           	print("Invalid choice. Please enter a number from the list or 'e' to exit.")
	           	
	       elif choice == 'e':
	       	break
	       else:
	               
	       	print("Invalid choice. Please enter a number from the list or 'e' to exit.")
	       	
	       
		
	def pick_up(self):
		
		"""
		Have this accept the returned object of the choose?
		
		If the room has any items, the method asks for a str
		of what the player wants to pick up. It then checks 
		to see if the chosen item is in the current room. If so, it
		indexes that item, removes it from the room list and 
		adds it to the player's inventory. 
		"""
		
		if self.current_room.items:
			
			
			pick_up_command = self.get_item_choice(self.current_room.items)
			
			"""
			Eventually add pick up and drop all?
			"""
			
			if pick_up_command in self.current_room.items:
			    
			    #Can the dict class call go directly into check_weight?
			    #player must enter the key exactly. Is there a way to use numbers? 
			    new_item = self.current_room.items[pick_up_command]
			    check_1 = self.check_weight(new_item.weight)
			    
			    if check_1:
			    	
			    
			    	if new_item is not None:
			    		new_item = self.current_room.items.pop(pick_up_command, None)
			    		self.inventory[pick_up_command] = new_item
			    		print(f"You pick up a {new_item.get_name()}")
			    	else:
			    		print("You can't pick that up!")
			    		
			    else:
			    	print("You can't pick that up.")
		
		else:
			print("There is nothing there.")
		
	def drop(self):
			
			"""
			Same as above but for dropping items.
			"""
			
			if self.inventory:
				drop_command = self.get_item_choice(self.inventory)
					
				if drop_command in self.inventory:
				   	dropped_item = self.inventory.pop(drop_command, None)
				   	if dropped_item is not None:
				   		self.current_room.items[drop_command] = dropped_item
				   		self.current_weight -= dropped_item.weight
				   		print(f"You drop a {dropped_item.get_name()}")
				else:
					print("You can't drop that!")
			
			else:
				print("Your inventory is empty.")
				
	def cast_spell(self):
		choosing = True
		while choosing:
			print("What spell would you like to cast?")
			for s in self.spells:
				count = self.spells.index(s)+1
				print(f"{count} - {s}")
			
			choice = int(input(">"))
			choice = choice-1
			if choice in self.spells:
			  
			    pick = self.spells[choice]
			    if pick == "Remove Curse":
				    print("What item do you want to uncurse?")
				    for i in self.inventory:
					    if self.inventory[i].cursed is True:
						    print(f"All curses have been removed!")
						    self.inventory[i].cursed = False
				    for i in self.equipped:
					    if self.equipped[i].cursed is True:
						    print(f"All curses have been removed!")
						    self.inventory[i].cursed = False
			else:
		            print("That is not a valid command.")
	