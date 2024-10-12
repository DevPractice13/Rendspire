from Rendspire.player import Player
from Rendspire.room import Room

class Command:
    """
    Command handling class.
    """

    def __init__(self, room_c = {}, combat_c ={}):
        
        self.room_c = room_c
        self.combat_c = combat_c
        self.running = True
        
        #game state flags, starting in_menu
        self.in_menu = True
        self.in_room = False
        self.in_combat = False
    
    def enter_combat(self):
    	"""
    	When the player changes state, i.e. moves from a room to
    	combat or to the main menu, these functions will set the 
    	flag for the current state to True and all other states to
    	False.
    	"""
    		
    	self.in_menu =  False
    	self.in_room = False
    	self.in_combat = True
    
    def enter_room(self):
    	self.in_menu =  False
    	self.in_room = True
    	self.in_combat = False
    	#player.move()
    
    def enter_menu(self):
    	self.in_menu =  True
    	self.in_room = False
    	self.in_combat = False
    	#show_menu()

    def recieve_input(self, main_command, arg_1 = None, arg_2 = None):
        """
        
        Instead of doing all this flag checking... just pass the current command
        set when its needed. When in combat, input is taken with combat commands passed, when in 
        room, with room commands etc. 
        
        Or have a current_commands variable that gets changed to the necessary 
        set before asking for input. 
        """
        
        #This is only useful for room commands:
        if self.in_room:
        
        	valid_dir = ['n', 's', 'e', 'w']
        
        	main_command = input('>')
        	if main_command in self.room_c:
        		if main_command in valid_dir:
        			self.room_c[main_command](main_command)
        		else:
        			self.room_c[main_command]()
        			if main_command == 'q':
        				inval = True
        				return inval
        		
        	else:
        		print("That is an invalid command.")
        		inval = True
        		return inval
        
        if self.in_combat:
        	if main_command in self.combat_c:
        		print("You are in combat")
        		self.combat_c[main_command](arg_1, arg_2)
        
        	else:
        		print("That is an invalid command.")
        		inval = True
        		return inval
   
        	
        	
        
        		
       
        	
    		
    		
    		
