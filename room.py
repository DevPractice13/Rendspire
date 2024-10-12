class Room: 
	
	def __init__(self, connection_list = False,in_room=False, description="Empty", items = {}, is_lit = True, story_beat = False, story_name = False):
		#flag for when the player is in the room
		#to add: lighting, doors
		#Add permanent lighting and temporary lighting 
		
		self.story_beat = story_beat
		#so the player can be asked if they are sure they want to interact with something
		self.story_name = story_name
		
		"""
		Adding a story beat method from the story class to be shown if the player interacts with a 
		story element. 
		"""
		
		self.connection_list = connection_list
		self.in_room = in_room 
		self.description = description
		self.items = items
		self.is_lit = is_lit 
		
		#This will tell whether the exits are locked or not.
		#Add another checker to change room whether they are locked or not
		#Then add a use_key function to unlock in a chosen direction
		self.locked_list = {}
		
		#Instances will be passed their connecting rooms, probably make a default False
		#instance can't reference a room that hasn't been instantiated yet. 
		#self.connections = {"n": n_con, "s": s_con, "e": e_con, "w": w_con}
		
	#play story beat
	def play_story(self):
		self.story_beat()
		
	def show_connections(self):
		print(self.connection_list)
		
	def get_connection(self, direction):
		return self.connection_list[direction]
		
	def display_items(self):
	   	"""Display items with numbered choices.
	   	Uses the instance name. 
	   	
	   	"""
	   	
	   	for i, (item_name, item_obj) in enumerate(self.items.items(), start=1):
	   	   print(f"{i} - {item_obj.name}")
		
	def describe_room(self):
		
		if self.is_lit:
			print(self.description,'\n')
			if self.items:
				print("These are the items in the room:\n")
				"""
				for i in self.items:
				
				#shows the name attribute of the item instance
					print(i)
				"""
				self.display_items()
		
		else:
			print("It's pitch black!")
	
	
		
	