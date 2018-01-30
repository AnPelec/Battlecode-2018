# missing functions
#  * HEAL ... DONE
#  * OVERCHARGE

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

class HealerClass(object):

	def heal_bitch(self, unit):
		if not gc.is_heal_ready(unit.id):
			return
			
		location = unit.location
		nearby = gc.sense_nearby_units(location.map_location(), unit.attack_range(), my_team)
		for other in nearby:
			if gc.can_heal(unit.id, other.id):
				# print('healed a friend!')
				gc.heal(unit.id, other.id)
				return
			
	def overcharge_attack(self, unit):
		if not gc.is_overcharge_ready(unit.id):
			return
		if bc.ResearchInfo.get_level(bc.UnitType.Healer) < 3:
			return
			
		location = unit.location
		
		possible_targets = sense_nearby_units_by_team(location.map_location(), unit.ability_range(), my_team)
		for other in possible_targets:
			if gc.can_heal(unit.id, other.id):
				gc.heal(unit.id, other.id)
				return
