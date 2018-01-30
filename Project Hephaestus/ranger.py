# missing functions
#  * ATTACK ... in General
#  * SNIPE

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

class RangerClass(object):

	def __init__(self):
		self.marsMap = bc.GameMap.mars_map
		self.earthMap = bc.GameMap.earth_map
		
		self.marsHeight = self.marsMap.height
		self.marsWidth = self.marsMap.width
		
		self.earthHeight = self.earthMap.height
		self.earthWidth = self.earthWidth.width
		
		self.NUMBER_OF_GUESSES = 5

	def snipe_attack_mars(self, unit):
		if unit.ranger_is_sniping():
			return
		if not gc.is_begin_snipe_ready(unit.id):
			return
		if bc.ResearchInfo.get_level(bc.UnitType.Ranger) < 3:
			return
			
		for guess in range(self.NUMBER_OF_GUESSES):
			i = random.randint(0, self.marsHeight-1)
			j = random.randint(0, self.marsWidth-1)
			
			try:
				temp_location = bc.MapLocation(bc.Planet.Mars, i, j)
				if gc.can_begin_snipe(unit.id, temp_location):
					gc.begin_snipe(unit.id, temp_location)
					return
					
			except Exception as e:
				print('Error:', e)
				# use this to show where the error was
				traceback.print_exc()

	def snipe_attack_earth(self, unit):
		if unit.ranger_is_sniping():
			return
		if not gc.is_begin_snipe_ready(unit.id):
			return
		if bc.ResearchInfo.get_level(bc.UnitType.Ranger) < 3:
			return
			
		location = unit.location
		
		possible_targets = sense_nearby_units_by_type(location.map_location(), unit.ability_range(), bc.UnitType.Rocket)
		for other in possible_targets:
			if gc.can_begin_snipe(unit.id, other.location.map_location()):
				gc.begin_snipe(unit.id, other.location.map_location())
				return
				
		possible_targets = sense_nearby_units_by_type(location.map_location(), unit.ability_range(), bc.UnitType.Factory)
		for other in possible_targets:
			if gc.can_begin_snipe(unit.id, other.location.map_location()):
				gc.begin_snipe(unit.id, other.location.map_location())
				return
				
		for guess in range(self.NUMBER_OF_GUESSES):
			i = random.randint(0, self.earthHeight-1)
			j = random.randint(0, self.earthWidth-1)
			
			try:
				temp_location = bc.MapLocation(bc.Planet.Earth, i, j)
				if gc.can_begin_snipe(unit.id, temp_location):
					gc.begin_snipe(unit.id, temp_location)
					return
					
			except Exception as e:
				print('Error:', e)
				# use this to show where the error was
				traceback.print_exc()
