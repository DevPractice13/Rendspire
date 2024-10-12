import random
from Rendspire.command import Command
from Rendspire.enemy import Enemy
from Rendspire.player import Player
from Rendspire.room import Room 
from Rendspire.combat import Combat
from Rendspire.story import Story

"""
When my enemies have a positve speed, it breaks the combat commands. 

Game is moving forward even with an invalid command, need these
to not move the game forward. 

Will have to move to while loops for input to keep from moving 
the turns forward on an invalid command. 
"""
peaceful = True

#enemy instance test
d_sentinel_orb = Enemy('Damaged Sentinel Orb', 5, 6, 2, 1, 4, 'A cracked orb the dull grey color of a darkening sky floating in midair.')
enthralled_goblet = Enemy('Enthralled Goblet', 6, 3, 3, 10, 0, 'A smaller, hunched version of a Goblin, controlled by some mystic force.')
bleakwurm = Enemy('Bleak Wurm', 4, 3, 2, 10, 0, 'A small, wingless dragon.')
#boss test
dark_knight = Enemy('Black Knight', 4, 3, 2, 1, 0, 'A scary black knight.')

#enemy list
area_1_enemies = [bleakwurm, enthralled_goblet]

#make a boss list?

class Main:
    """main game class.
    Runs the main loop and handles general settings, loading, saving, quiting.
    """
    

    def __init__(self, new_player, settings=True, in_menu=True, running=True, turn_count = 0, story = False):
        # potential settings, unused
        self.settings = settings
        self.new_player = new_player
        self.turn_count = turn_count
        #This will just be to show the initial story intro that requires no interaction
        self.story = story
        
        # running flag to keep the game running in the main loop
        self.running = running
        
    def turn_add(self):
     	self.turn_count += 1
     
    def show_turns(self):
     	print(f"\nTurn: {self.turn_count}\n") 
     
    def show_coms(self):
     	"""
     	Prints the command list.
     	"""
     	
     	command_help_list =  """q - Quit\ni - View inventory\neq - Equip\nu - Unequip\nseq - View equipment\nn - Move north\ns - Move south
e - Move east\nw - Move west\np - Pick up\nd - Drop\nin - Interact\nk - Use Key\nsn - Snuff Out Candle"""
     	print(command_help_list)
 
    def main_loop(self, command):
    	"""main game loop"""
    	
    	#print("Welcome to Rendspire.\n")
    	#print("Press 'n' to start a new game.")
    	
    	self.story.start_story()
    	 
    	while self.running:
    		"""introduce the menu and recieve input"""
    		
    		#main_command = input('>')
    		#command.enter_combat()
    		#if main_command == 'n':
    		"""
    		New game starts. Player enters first room
    		"""
    		command.enter_room()
    		self.new_player.current_room.describe_room()
    			
    			
    		#else:
    		#print("That is not a valid command.")
    			
    			
    		while command.in_room and self.running:
    			
    			"""
    			Room movement loop.
    			Add a way to not add turn counter if an invalid command or quit menu is entered. 
    			"""
    			
    			
    			turn_check = command.recieve_input(command)
    			
    			if self.story.crystal_finished:
    				print("You are fighting the boss.")
    				self.combat_check(command, True, dark_knight)
    				self.story.area_2_start()
    				self.new_player.teleport()
    				self.story.crystal_finished = False
    			#Check for a special count
    			#if self.new_player.counting:
    				#self.new_player.special_turn_count +=1
    				#print(self.new_player.special_turn_count)
    			self.new_player.show_light()
    			self.new_player.update_candle()
    			
    			
    			if turn_check is not True:
    				self.turn_add()
    				self.show_turns()
    			
    			#if self.running:
    			fc = self.combat_check(command)
    			
    			
    			if fc == True:
    				self.new_player.current_room.describe_room()
    				fc = False
    		
    def combat_check(self, current_command, encounter = False, set_enemy = False):
    	"""
    	Checks for random encounters. Will need to check for running here 
    	as well. 
    	
    	Adding an option to enter a set enemy such as a boss. 
    	
    	Encounter attribute tells us whether this is a garunteed fight. 
    	"""
    	if peaceful is False:
    		com_chance = random.randrange(1,5)
    		if com_chance == 1 or com_chance == 2 or encounter:
    			
    			current_command.enter_combat()
    			
    			#check to see if this is a set encounter
    			if encounter:
    				current_enemy = set_enemy
    			else:
    				current_enemy = random.choice(area_1_enemies)
    			print(f"A {current_enemy.name} appears!")
    	
    			fight = Combat()
    		
    			initiative = fight.initiative(self.new_player.speed, current_enemy.speed)
    			in_combat = True
    	
    			if initiative:
    				while in_combat:
    					player_input = input('>')
    					inval_check = current_command.recieve_input(player_input, self.new_player, current_enemy)
    					if inval_check == True:
    						print("always invalid")
    						continue
    					self.turn_add()
    					self.show_turns()
    					fight.attack_v_defense(current_enemy, self.new_player)
    		
    			
    					self.new_player.undefend()
    			
    					self.new_player.show_stats()
    
    			
    					self.turn_add()
    					self.show_turns()
    					if self.new_player.current_health <= 0:
    						print(f"You died on turn {self.turn_count}!")
    						in_combat = False
    						self.running = False
    						return self.running
    					if current_enemy.current_health <= 0:
    						print("You won!")
    						in_combat = False
    						current_command.enter_room()
    						finished_combat = True
    						return finished_combat
    					if self.new_player.ran:
    						
    						in_combat = False
    						current_command.enter_room()
    						finished_combat = True
    						return finished_combat
    						#Have to add another version of combat for the enemy going first.
    			else:
    					
    					while in_combat:
    						fight.attack_v_defense(current_enemy, self.new_player)
    						self.new_player.undefend()
    						player_input = input('>')
    						inval_check = current_command.recieve_input(player_input, self.new_player, current_enemy)
    						if inval_check == True:
    							
    							continue
    						self.turn_add()
    						self.show_turns()
    					
    		
    			
    					
    			
    						self.new_player.show_stats()
    
    			
    						self.turn_add()
    						self.show_turns()
    						if self.new_player.current_health <= 0:
    							print(f"You died on turn {self.turn_count}!")
    							in_combat = False
    							self.running = False
    							return self.running
    						if current_enemy.current_health <= 0:
    							print("You won!")
    							in_combat = False
    							current_command.enter_room()
    							finished_combat = True
    							return finished_combat
    						if self.new_player.ran:
    						
    							in_combat = False
    							current_command.enter_room()
    							finished_combat = True
    							return finished_combat
    					
    
    		
    def quit(self):
        """
       Asks to make sure the user wants to quit, then
       returns the running flag as false.
       """ 
        print("Are you sure you want to quit? y/n")
        sure_quit = input('>')
        if sure_quit == 'y':
        		
        	#slight bug here, still says command was valid 
        	#if you input invalid command instead of 'y'
        	self.running = False
        	non_turn = False
        	return self.running, non_turn
   
        
        	
    		
    		
    		
