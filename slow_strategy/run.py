import battlecode as bc
import random
import sys
import traceback

import os
print(os.getcwd())

print("pystarting")

# A GameController is the main type that you talk to the game with.
# Its constructor will connect to a running game.
gc = bc.GameController()
directions = list(bc.Direction)
my_team = gc.team()

print("pystarted")

# It's a good idea to try to keep your bots deterministic, to make debugging easier.
# determinism isn't required, but it means that the same things will happen in every thing you run,
# aside from turns taking slightly different amounts of time due to noise.
random.seed(6137)
		
def get_karbonite(unit):
	for dir in bc.Direction:
		if gc.can_harvest(unit.id, dir):
			#print('harvested karbonite!')
			gc.harvest(unit.id, dir)
			continue
			
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
			
def random_move(unit):
	dir = random.choice(directions)
	if gc.is_move_ready(unit.id) and gc.can_move(unit.id, dir):
		gc.move_robot(unit.id, dir)
		#print('Moved successfully!')
		
def build_blueprint(unit, building_type):
	for dir in bc.Direction:
		if gc.karbonite() > building_type.blueprint_cost() and gc.can_blueprint(unit.id, building_type, dir):
			gc.blueprint(unit.id, building_type, dir)
		
def complete_build(unit, building_type):
	location = unit.location
	if location.is_on_map():
		nearby = gc.sense_nearby_units(location.map_location(), 2)
		for other in nearby:
			if other.unit_type == building_type and gc.can_build(unit.id, other.id):
				gc.build(unit.id, other.id)
				#print('built a thing!')
				# move onto the next unit
				continue	

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
	
def load_rocket(unit):
	location = unit.location
	if location.is_on_map():
		#print('eisai mia poulla')
		nearby = gc.sense_nearby_units(location.map_location(), 2)
		for other in nearby:
			if gc.can_load(unit.id, other.id):
				print('loaded rocket!')
				gc.load(unit.id, other.id)
	
def get_free_location():
	map_of_mars = gc.starting_map(bc.Planet.Mars)
	height = map_of_mars.height
	width = map_of_mars.width
	
	for i in range(height):
		for j in range(width):
			try:
				temp_loc = bc.MapLocation(bc.Planet.Mars, i, j)
				if map_of_mars.is_passable_terrain_at(temp_loc):
					print('found free location on mars!')
					return temp_loc
					
			except Exception as e:
				print('Error:', e)
				# use this to show where the error was
				traceback.print_exc() 
	
def update_team_array(free_loc):
	team_array = gc.get_team_array(bc.Planet.Earth)
	next_idx = team_array[0]
	
	if next_idx < 32:
		gc.write_team_array(next_idx, free_loc.x)
		gc.write_team_array(next_idx+1, free_loc.y)
		gc.write_team_array(0, next_idx+2)
	
def has_landed_before(free_loc):
	target_x = free_loc.x
	target_y = free_loc.y
	
	team_array = gc.get_team_array(bc.Planet.Earth)
	next_idx = team_array[0]
	
	for i in range(1, next_idx, 2):
		if team_array[i] == target_x and team_array[i+1] == target_y:
			return True
	
	return False
	
def launch_rocket(unit):
	if not unit.location.is_on_map():
		return
	garrison = unit.structure_garrison()
	if len(garrison) > 0:
		free_loc = get_free_location()
		if (gc.can_launch_rocket(unit.id, free_loc)) and (not has_landed_before(free_loc)):
			print('launched rocket!')
			update_team_array(free_loc)
			gc.launch_rocket(unit.id, free_loc)

def unload_rocket(unit):
	if unit.rocket_is_used():
		garrison = unit.structure_garrison()
		if len(garrison) > 0:
			d = random.choice(directions)
			if gc.can_unload(unit.id, d):
				#print('unloaded a poulla!')
				gc.unload(unit.id, d)
				
gc.queue_research(bc.UnitType.Rocket)
gc.queue_research(bc.UnitType.Worker)
gc.queue_research(bc.UnitType.Knight)
	
gc.write_team_array(0, 1)  # how many values are used
	
while True:
    # We only support Python 3, which means brackets around print()
	print('pyround:', gc.round(), 'time left:', gc.get_time_left_ms(), 'ms')
	
	try:
		for current_unit in gc.my_units():
		
			if current_unit.unit_type == bc.UnitType.Worker:
				get_karbonite(current_unit)
				if gc.round() < 10:
					random_move(current_unit)
				elif gc.round() < 20:
					complete_build(current_unit, bc.UnitType.Factory)
					build_blueprint(current_unit, bc.UnitType.Factory)
					random_move(current_unit)
				else:
					complete_build(current_unit, bc.UnitType.Rocket)
					build_blueprint(current_unit, bc.UnitType.Rocket)
					if gc.round()%3 == 0:
						random_move(current_unit)
				
			if current_unit.unit_type == bc.UnitType.Knight:
				pass
				
			if current_unit.unit_type == bc.UnitType.Mage:
				pass
				
			if current_unit.unit_type == bc.UnitType.Ranger:
				pass
				
			if current_unit.unit_type == bc.UnitType.Healer:
				pass
				
			if current_unit.unit_type == bc.UnitType.Factory:
				unload_factory(current_unit)
				if gc.round()%2 == 0:
					produce_unit(current_unit, bc.UnitType.Worker)
				else:
					produce_unit(current_unit, bc.UnitType.Knight)
				
			if current_unit.unit_type == bc.UnitType.Rocket:
				launch_rocket(current_unit)
				load_rocket(current_unit)
				unload_rocket(current_unit)
				
	except Exception as e:
		print('Error:', e)
		# use this to show where the error was
		traceback.print_exc()
			
    # send the actions we've performed, and wait for our next turn.
	gc.next_turn()

    # these lines are not strictly necessary, but it helps make the logs make more sense.
    # it forces everything we've written this turn to be written to the manager.
	sys.stdout.flush()
	sys.stderr.flush()
