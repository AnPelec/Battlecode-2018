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

class RocketClass(object):

	def __init__(self):
		self.marsMap = bc.GameMap.mars_map
		
		self.marsHeight = self.marsMap.height
		self.marsWidth = self.marsMap.width
		
		self.NUMBER_OF_GUESSES = 5

	def get_free_location(self, unit):
	
		for guess in range(self.NUMBER_OF_GUESSES):
			i = random.randint(0, self.marsHeight-1)
			j = random.randint(0, self.marsWidth-1)
			temp_location = bc.MapLocation(bc.Planet.Mars, i, j)
			try:
				if gc.can_launch_rocket(unit.id, temp_loc):
					print('found free location on mars!')
					return temp_location
						
			except Exception as e:
				print('Error:', e)
				# use this to show where the error was
				traceback.print_exc()
						
		return bc.MapLocation(bc.Planet.Mars, 0, 0)

	def launch_rocket(unit):
		garrison = unit.structure_garrison()
		if len(garrison) > 0:
			#print('prepare for launch')
			free_loc = get_free_location(unit)
			
			if gc.can_launch_rocket(unit.id, free_loc):
				#print('launched rocket!')
				#update_team_array(free_loc)
				gc.launch_rocket(unit.id, free_loc)
				
	def unload_rocket(unit):
		garrison = unit.structure_garrison()
		if len(garrison) > 0:
			d = random.choice(directions)
			if gc.can_unload(unit.id, d):
				#print('unloaded a poulla!')
				gc.unload(unit.id, d)
		else:
			gc.disintegrate_unit(unit.id)
