

class Story:
	
	"""
	Class to handle story elements and progression flags.
	Stort beats will be held in methods. These methods will check for progression flags.
	The methods will be passed into room instances as the optional "story" attribute. 
	
	The Story method will be activated when interacted with by the player. 
	
	We will start by testing start and the skeleton - painting move.
	
	A way to have automatic story beats? A needed interact == True flag for interaction based ones? 
	
	Boss - Main handles combat but it's defaulted to random. Should we keep combat related loops 
	in main and import here with the current_enemy = Boss_1. '
	
	Painting finished set to true to test second area. 
	"""
	
	def __init__(self, start_finished= False, skeleton_finished=False, painting_finished=True, crystal_finished=False, start_2_finished =False):
		
		#progression flags
		self.start_finished = start_finished
		self.skeleton_finished = skeleton_finished
		self.painting_finished = painting_finished
		self.crystal_finished = crystal_finished
		self.start_2_finished = start_2_finished
		
	def start_story(self):
		"""
		Provides the intro narrative and access to the skeleton story beat. 
		Unlike the interactable methods below, this will be called automatically
		at the start of the game. 
		"""
		if self.start_finished is False:
			
			print("Welcome, brave adventurer.\n\n")
			print("Don't know the commands? Tough luck knave!\n\n")
			print("Just kidding... after pressing 'n' then enter to start a new game press 'c' then enter to see a list of commands.\n\n")
			print("In a hollow on the windswept heath, you have finally found a way in. A way to avoid the wraiths that circle.")
			print("the castle above. A door so smooth and ancient it seems to be a petrified tree encased in rock. Strangely")
			print("the lock seems to have rotted before the wood and you push it open with ease.\n")
			print("You enter Rendspire, perhaps the first guest of Lord Talibrand who was not wraith or goblin-kin in an age.")
			self.start_finished = True
			
	def skeleton(self):
		
		if not self.skeleton_finished:
			
			print("Here lies a skeleton in a dusty chainmail shirt and a menacing helm.")
			print("He turns his head towards you and his jaw creaks as an otherworldy voice says:")
			print("If he wants the knife so badly, he can take it.\n")
			print("The skeleton hands you a twisted dagger.")
			self.skeleton_finished = True
			
		else:
			
			print("The skeleton looks as though it had never moved.")
			
	def painting(self):
			
			if self.skeleton_finished is True:
				
				print("Thank you for finding this! Now I can finally rest in peace.")
				self.painting_finished = True
				
			else:
				
				print("You see a faded painting of a nobleman. The eyes seems to follow you around the room...")
				
	def crystal_ball(self):
			
			if self.painting_finished:
				
				
				
				print("You place your hand on the crystal and whisper the spell... A thunderous roar shakes the ground.")
				
				self.crystal_finished = True
			
			else:
				print("You see a dusty grey orb.")
				
	def area_2_start(self):
			
			"""
			The Starting story flag for the second set of rooms.
			"""
			
			print("The air seems slightly less stifiling here.")
			self.start_2_finished = True
			
			
		