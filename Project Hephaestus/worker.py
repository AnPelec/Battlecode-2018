# missing functions
#  * HARVEST ... DONE
#  * BLUEPRINT ... DONE
#  * BUILD ... DONE
#  * REPAIR ... TODO
#  * REPLICATE ... DONE
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

class WorkerClass(object):

	def harvest_karbonite(unit):
		dir = random.choice(directions)
		if gc.can_harvest(unit.id, dir):
			#print('harvested karbonite!')
			gc.harvest(unit.id, dir)
		
	def build_blueprint(unit, building_type):
		dir = random.choice(directions)
		if gc.karbonite() > building_type.blueprint_cost() and gc.can_blueprint(unit.id, building_type, dir):
			gc.blueprint(unit.id, building_type, dir)
			
	def repair(unit):
		nearby = gc.sense_nearby_units_by_type(unit.location.map_location(), 2, bc.UnitType.Factory)
		for other in nearby:
			if gc.can_repair(unit.id, other.id):
				gc.repair(unit.id, other.id)
				return
		
		nearby = gc.sense_nearby_units_by_type(unit.location.map_location(), 2, bc.UnitType.Rocket)
		for other in nearby:
			if gc.can_repair(unit.id, other.id):
				gc.repair(unit.id, other.id)
				return
		
			
	def replicate_worker(unit):
		dir = random.choice(directions)
		if gc.can_replicate(unit.id, dir):
			gc.replicate(unit.id, dir)
			
	def complete_build(unit, building_type):
		nearby = gc.sense_nearby_units_by_type(unit.location.map_location(), 2, building_type)
		for other in nearby:
			if gc.can_build(unit.id, other.id) and not gc.structure_is_built(other.id):
				gc.build(unit.id, other.id)
				break