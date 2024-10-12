from Rendspire.command import Command
from Rendspire.player import Player
from Rendspire.enemy import Enemy
from Rendspire.room import Room 
from Rendspire.main import Main
from Rendspire.item import Weapon, Armor, Consumable, Lightsource, Spellbook
from Rendspire.combat import Combat
from Rendspire.story import Story
from Rendspire.spells import Spell
import json
import pickle
from pathlib import Path

"""
to add: player name and tombstone, leveling, spells or special abilities, in room objects, chests etc, traps, multiple story beats in one room? 
"""

#Save test

#new story instance
new_story = Story()

#new item instances for testing class instance lists
r_sword = Weapon("Rusty Sword", 7, "An old sword", "weapon", 2)
r_sword_2 = Weapon("Rusty Sword", 7, "An old sword", "weapon", 2)
#Key: RS2
i_sword = Weapon("Iron Sword", 7, "A basic iron sword", "weapon", 4)
l_armor = Armor("Leather Armor", 5, "Padded leather armor", "armor", 2)
potion = Consumable("Health Potion", 1, "A healing draught.", "consumable", 5)
key = Consumable("Key", 0, "A rusty key.", "key", 0)
key_2 = Consumable("Key", 0, "A rusty key.", "key", 0)

#a candle
candle = Lightsource("Candle", 1, "A tallow candle.", "lightsource", 10)

#A cursed item
c_helmet = Armor("Horned Helmet", 6, "A strange, evil looking helmet.", "armor", -3, True)

#spells
#new_spells = Spell()

#spellbook
#remove_curse = Spellbook("Remove Curse", 1, "Remove curse spell", "spellbook", new_spells.remove_curse())


"""
Only using dictionaries and keys is not robust. Give unique keys but display the name from the instance itself? 
Now all instances have unique instance and keys but the multiples will have the same name attributes and stats.
They will be chosen and moved by their number and their name attribute will be displayed, not their key. 
"""

#Area 1
room_1 = Room(False, description = "This is the first room", items = {"Candle": candle,"Rusty Sword": r_sword, "RS2": r_sword_2,"Health Potion": potion, "Key": key, "Key_2": key})
#the room with a story beat will take the story method and probably a name for an interact choice? 
room_2 = Room(False, description = "This is the second room", items = {"Iron Sword": i_sword, "Leather Armor": l_armor}, story_beat = new_story.skeleton, story_name = "Skeleton")
room_3 = Room(False, description = "You guessed it, the THIRD room.", story_beat = new_story.painting, story_name = "Painting")
room_4 = Room(False, description = "A stone room with a cloudy orb on a pedestal in the corner.", items = {"Horned Helmet": c_helmet}, is_lit = True, story_beat = new_story.crystal_ball, story_name = "Crystal Ball")

all_rooms = [room_1, room_2, room_3, room_4]

#Room connection lists. Possible data class this?
#These are the inital room instances. They will need to take the loaded
#instances if it's not a new game. '
room_1.connection_list = {"n": room_2}
room_2.connection_list = {"s": room_1, "e": room_3, "n": room_4}
room_3.connection_list = {"w": room_2}
room_4.connection_list = {"s": room_2}

#locked list test
room_2.locked_list["n"] = True
room_2.locked_list["e"] = True

#spells


#Area 2
room_5 = Room(False, description = "A dank chamber where light from a distant hole in the roof shimmers off the moist walls.", items = {})

#Area 2 connections
room_5.connection_list = {}
#Area 2 locked list

print(type(all_rooms))
#Test saving player class instead
def save_game(filename, instance):
    print(f"Saving all_rooms: {instance}")
    with open(filename, 'wb') as file:
        pickle.dump(instance, file)

def load_game(filename):
    print("it loaded")
    f_test = Path(filename)
    if f_test.exists():
    	print(f"Loaded {filename}")
    	with open(filename, 'rb') as file:
        	return pickle.load(file)
        
print(type(all_rooms))
all_rooms = load_game("all_rooms_save.pkl")
l_story = load_game("load_story.pkl")
l_player = load_game("load_player.pkl")
print(all_rooms[0].description)
#works for room 1

print(type(all_rooms))

new_room = all_rooms[0]
#this needs to take in a loaded player and story if the player is loading. 
print("Welcome to Rendspire. Would you like to start a new game or load?")
print("Enter 'n' for new game and 'l' to load")
inp = input(">")

if_start = True
while if_start:
	if inp == "l":
		player_1 = l_player
		new_story = l_story
		if_start = False
	elif inp == "n":
		player_1 = Player(room_1, room_5)
		if_start = False
	else:
		print("That is an invalid command.")

game = Main(player_1, story = new_story)

combat_1 = Combat()

#new command dictionary test
room_coms = {'n': player_1.move, 's': player_1.move, 'e': player_1.move, 'w': player_1.move, 
							'p': player_1.pick_up, 'd': player_1.drop, 'i': player_1.show_inventory, 'q': game.quit,
							"eq": player_1.equip, "seq": player_1.show_equipment, "c": game.show_coms, "u": player_1.unequip, 
							"k": player_1.use_key, "sn": player_1.snuff_out, "in": player_1.interact, "cs": player_1.cast_spell}

combat_coms = {'a': combat_1.attack_v_defense, 'd': player_1.defend, 'i': player_1.equip, 'r': combat_1.run}
							
command_1 = Command(room_coms, combat_coms)
"""
The main game loop now takes an instance of the command module and only handles 
the main loop.
"""
test_file_name =  Path("DnDPython/all_rooms_save.pkl")

game.main_loop(command_1)

save_game("all_rooms_save.pkl", all_rooms)
save_game("load_story.pkl", new_story)
save_game("load_player.pkl", player_1)






