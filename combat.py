import random

class Combat:
	"""
	A class to handle the combat loop.
	"""
	
	def __init__(self, ran = False):
		self.ran = ran
		
	def initiative(self, player_speed, enemy_speed):
		"""
		A method to compare the player and enemy's speed stat.
		The highest speed will go first.
		"""
		if player_speed >= enemy_speed:
			player_first = True
			return player_first 
		
		else:
			player_first = False
			return player_first
			
	def run(self, player_speed, enemy_speed):
			"""
			A method to see if a player can run from an enemy.
			"""
			
			win_chance = random.randrange(1,3)
			lose_chance = random.randrange(1,10)
			
			if player_speed.speed >= enemy_speed.speed:
				if win_chance == 1 or win_chance == 2:
					print("You ran away!")
					player_speed.ran = True
					
				else:
					print("You can't escape!")
			else:
				if lose_chance == 1:
					print("You ran away!")
					player_speed.ran = True
					
				else:
					print("You can't escape!")
				
			
	def attack_v_defense(self, attacker, defender):
		"""
		Compare the attack to the defense stat and reduces the health by 
		the damage number if the attack is higher than defense.
		"""
		
		if attacker.attack >= defender.defense:
			#change this to say whether its you or the enemy attacking
			#This is not actually modifying their health
			print(f"You deal {attacker.damage} damage.")
			defender.current_health -= attacker.damage
		
		else:
			print("The attack does nothing.")
			
	def combat_loop(self, player, enemy, combat_commands):
		"""
		The combat loop. It first checks to see who has the initiative. 
		Then it automatically loops through the sequence of attacks untill the 
		player or enemy dies. 
		
		It will accept an instance of combat_commands for the player
		to choose actions. 
		
		"""
		
		initiative = self.initiative(player.speed, enemy.speed)
		
		in_combat = True
		
		if initiative:
			while in_combat:
				player_input = input('>')
				combat_commands.recieve_input(player_input, player, enemy)
				self.attack_v_defense(enemy, player)
				if player.health <= 0:
					print("You died!")
					in_combat = False
					player_dead = True
					return player_dead 
			
				if enemy.health <= 0:
					print("You won!")
					in_combat = False
					

			
		
		
		
		
		