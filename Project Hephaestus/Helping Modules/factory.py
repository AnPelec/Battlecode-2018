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

class FactoryClass(object):

	def unload_factory(unit):
		garrison = unit.structure_garrison()
		if len(garrison) > 0:
			d = random.choice(directions)
			if gc.can_unload(unit.id, d):
				#print('unloaded a poulla!')
				gc.unload(unit.id, d)
			
	def produce_unit(unit, product_type):			
		if gc.can_produce_robot(unit.id, product_type):
			gc.produce_robot(unit.id, product_type)
			#print('produced a poulla!')
