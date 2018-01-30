# missing functions
#  * ATTACK ... in General
#  * JAVELIN ... TODO

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

class KnightClass(object):

	def javelin_attack(self, unit):
		if not gc.is_javelin_ready(unit.id):
			return
		if bc.ResearchInfo.get_level(bc.UnitType.Knight) < 3:
			return
			
		location = unit.location
		
		possible_targets = sense_nearby_units_by_team(location.map_location(), unit.ability_range(), enemy_team)
		for other in possible_targets:
			if gc.can_javelin(unit.id, other.id):
				gc.javelin(unit.id, other.id)
				return
	
	
