# missing functions
#  * ATTACK ... in General
#  * BLINK

# MAKE DETERMINISTIC?

import battlecode as bc
import random
from datetime import datetime

gc = bc.GameController()
directions = list(bc.Direction)
my_team = gc.team()
enemy_team = bc.Team.Red
if my_team == bc.Team.Red:
	enemy_team = bc.Team.Blue
random.seed(datetime.now())

class GeneralActions(object):

	def move_bitch(unit):
		dir = random.choice(directions)
		if gc.is_move_ready(unit.id) and gc.can_move(unit.id, dir):
			gc.move_robot(unit.id, dir)
			#print('Moved successfully!')

	def attack_bitch(unit, p, place, attackType):
		if not gc.is_attack_ready(unit.id):
			return
	
		location = unit.location
		nearby = gc.sense_nearby_units_by_team(location.map_location(), unit.attack_range(), enemy_team)
		for other in nearby:
			if gc.can_attack(unit.id, other.id):
				#print('attacked a thing!')
				gc.attack(unit.id, other.id)
				continue
			
	def load_unit(unit):
		# possible improvement: go into the most crowded garrison
		nearby = gc.sense_nearby_units_by_type(unit.location.map_location(), 2, bc.UnitType.Rocket)
		for other in nearby:
			if gc.can_load(unit.id, other.id):
				gc.load(unit.id, other.id)
				break
	
	def move_and_expand(unit):
		# makes the robot move to the least crowded square
		# hoping that this is expanding the crowd
		moves = []
	
		location = unit.location
		for temp in range(9):
			dir = bc.Direction(temp)
			# center is direction 8 so it will always be last
			try:
				new_location = (location.map_location()).add(dir)
				nearby_units = gc.sense_nearby_units_by_team(new_location, 2, my_team)
				moves.append((len(nearby_units), temp))
			except Exception as e:
				print('Error:', e)
				# use this to show where the error was
				traceback.print_exc()			
				
		moves.sort()
		for tup in moves:
			if gc.is_move_ready(unit.id) and gc.can_move(unit.id, bc.Direction(tup[1])):
				gc.move_robot(unit.id, bc.Direction(tup[1]))
				#print('Moved successfully!')
				continue
	
	def move_and_shrink(unit):
		# makes the robot move to the least crowded square
		# hoping that this is expanding the crowd
		moves = []
	
		location = unit.location
		for temp in range(9):
			dir = bc.Direction(temp)
			# center is direction 8 so it will always be last
			try:
				new_location = (location.map_location()).add(dir)
				nearby_units = gc.sense_nearby_units_by_team(new_location, 2, my_team)
				moves.append((-1*len(nearby_units), temp))
			except Exception as e:
				print('Error:', e)
				# use this to show where the error was
				traceback.print_exc()			
					
		moves.sort()
		for tup in moves:
			if gc.is_move_ready(unit.id) and gc.can_move(unit.id, bc.Direction(tup[1])):
				gc.move_robot(unit.id, bc.Direction(tup[1]))
				#print('Moved successfully!')
				continue