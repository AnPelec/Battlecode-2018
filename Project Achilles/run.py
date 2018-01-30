import battlecode as bc
import random
import sys
import traceback
import json
from datetime import datetime

'''
from worker import WorkerClass
from knight import KnightClass
from mage import MageClass
from healer import HealerClass
from ranger import RangerClass
from factory import FactoryClass
from rocket import RocketClass
from general import GeneralActions
'''

import os
print(os.getcwd())

print("pystarting")

# A GameController is the main type that you talk to the game with.
# Its constructor will connect to a running game.
gc = bc.GameController()
directions = list(bc.Direction)
my_team = gc.team()
enemy_team = bc.Team.Red
if my_team == bc.Team.Red:
	enemy_team = bc.Team.Blue
random.seed(datetime.now())
	
print("pystarted")

# write in team array about the probabilities
# TODO:
#	implement research
#   implement probabilities
#   implement reinforcement learning

'''
filename = 'strategy.json'
data = json.load(open(filename))
'''

data = {
	"Mars": {
		"worker_harvest": 0.5,
		"worker_replicate": 1.0,
		"worker_attack": 1.0,
		"worker_move": 0.8,
		
		"knight_javelin": 0.7,
		"knight_attack": 1.0,
		"knight_move": 0.9,
		
		"mage_blink": 0.7,
		"mage_attack": 1.0,
		"mage_move": 0.9,
		
		"ranger_snipe": 0.7,
		"ranger_attack": 1.0,
		"ranger_move": 0.9,
		
		"healer_overcharge": 0.7,
		"healer_heal": 1.0,
		"healer_move": 1.0
	},
	"Earth": {
		"first_phase": {
			"threshold": 150,
			"worker_harvest": 0.3,
			"worker_replicate": 0.35,
			"worker_blueprint_factory": 0.65,
			"worker_blueprint_rocket": 0.8,
			"worker_repair": 0.8,
			"worker_attack": 0.75,
			"worker_move": 0.5,
			
			"produce_worker": 0.2,
			"produce_knight": 0.6,
			"produce_healer": 0.63,
			"produce_mage": 0.66,
			"produce_ranger": 0.85,
			"rocket_launch": 0.0
		},
		
		"emergency_attack": {
			"worker_harvest": 0.3,
			"worker_replicate": 0.35,
			"worker_blueprint_factory": 0.8,
			"worker_blueprint_rocket": 0.82,
			"worker_repair": 0.85,
			"worker_attack": 0.75,
			"worker_move": 0.5,
			
			"produce_worker": 0.05,
			"produce_knight": 0.45,
			"produce_healer": 0.55,
			"produce_mage": 0.65,
			"produce_ranger": 1.0,
			"rocket_launch": 0.0
		},
		
		"second_phase": {
			"threshold": 300,
			"worker_harvest": 0.4,
			"worker_replicate": 0.35,
			"worker_blueprint_factory": 0.45,
			"worker_blueprint_rocket": 0.9,
			"worker_repair": 1.0,
			"worker_attack": 1.0,
			"worker_move": 0.9,
			
			"produce_worker": 0.2,
			"produce_knight": 0.4,
			"produce_healer": 0.45,
			"produce_mage": 0.6,
			"produce_ranger": 0.7,
			"rocket_launch": 0.1
		},
		
		"third_phase": {
			"worker_harvest": 0.3,
			"worker_replicate": 0.6,
			"worker_blueprint_factory": 0.65,
			"worker_blueprint_rocket": 0.75,
			"worker_repair": 0.85,
			"worker_attack": 0.85,
			"worker_move": 0.8,
			
			"produce_worker": 0.2,
			"produce_knight": 0.5,
			"produce_healer": 0.55,
			"produce_mage": 0.6,
			"produce_ranger": 0.94,
			"rocket_launch": 0.8
		},
		
		"emergency_rocket": {
			"worker_harvest": 0.5,
			"worker_replicate": 0.5,
			"worker_blueprint_factory": 0.5,
			"worker_blueprint_rocket": 1.0,
			"worker_repair": 0.85,
			"worker_attack": 0.85,
			"worker_move": 0.8,
			
			"produce_worker": 0.1,
			"produce_knight": 0.2,
			"produce_healer": 0.3,
			"produce_mage": 0.4,
			"produce_ranger": 0.5,
			"rocket_launch": 0.0
		},
		
		"emergency_factory": {
			"worker_harvest": 0.5,
			"worker_replicate": 0.5,
			"worker_blueprint_factory": 1.0,
			"worker_blueprint_rocket": 1.0,
			"worker_repair": 0.85,
			"worker_attack": 0.85,
			"worker_move": 0.8,
			
			"produce_worker": 0.1,
			"produce_knight": 0.2,
			"produce_healer": 0.3,
			"produce_mage": 0.4,
			"produce_ranger": 0.5,
			"rocket_launch": 0.0
		},
		
		"knight_javelin": 0.6,
		"knight_attack": 1.0,
		"knight_move": 0.8,
		
		"mage_blink": 0.7,
		"mage_attack": 1.0,
		"mage_move": 0.9,
		
		"ranger_snipe": 0.5,
		"ranger_attack": 1.0,
		"ranger_move": 0.9,
		
		"healer_overcharge": 0.6,
		"healer_heal": 1.0,
		"healer_move": 1.0
	}
}

launch_probability = {
	13: 1.0,
	12: 1.0,
	11: 1.0,
	10: 1.0,
	9: 1.0,
	8: 0.8,
	7: 0.4,
	6: 0.2,
	5: 0.1,
	4: 0.05,
	3: 0.001,
	2: 0.0,
	1: 0.0,
	0: 0.0
}

gc.queue_research(bc.UnitType.Rocket)
gc.queue_research(bc.UnitType.Worker)
gc.queue_research(bc.UnitType.Knight)
gc.queue_research(bc.UnitType.Knight)
gc.queue_research(bc.UnitType.Ranger)
gc.queue_research(bc.UnitType.Worker)
gc.queue_research(bc.UnitType.Worker)
gc.queue_research(bc.UnitType.Ranger)
gc.queue_research(bc.UnitType.Ranger)
gc.queue_research(bc.UnitType.Knight)
gc.queue_research(bc.UnitType.Rocket)
gc.queue_research(bc.UnitType.Rocket)
gc.queue_research(bc.UnitType.Worker)
gc.queue_research(bc.UnitType.Mage)
gc.queue_research(bc.UnitType.Healer)
gc.queue_research(bc.UnitType.Mage)
gc.queue_research(bc.UnitType.Healer)
gc.queue_research(bc.UnitType.Mage)
gc.queue_research(bc.UnitType.Healer)
gc.queue_research(bc.UnitType.Mage)

def find_dimensions(current_planet):
	low = 19
	high = 49
	ansx = 19
	ansy = 19
	
	planet_map = gc.starting_map(current_planet)
	
	while (low <= high):
		med = (low + high)//2
		temp_location = bc.MapLocation(current_planet, med, 0)
		if planet_map.on_map(temp_location):
			if ansx < med:
				ansx = med
			low = med+1
		else:
			high = med-1
	
	low = 19
	high = 49
	while (low <= high):
		med = (low + high)//2
		temp_location = bc.MapLocation(current_planet, 0, med)
		if planet_map.on_map(temp_location):
			if ansy < med:
				ansy = med
			low = med+1
		else:
			high = med-1
			
	return (ansx, ansy)

marsMap = gc.starting_map(bc.Planet.Mars)
earthMap = gc.starting_map(bc.Planet.Earth)
(marsHeight, marsWidth) = find_dimensions(bc.Planet.Mars)
(earthHeight, earthWidth) = find_dimensions(bc.Planet.Earth)
locations = []
color_chosen = []
component = {}
NUMBER_OF_GUESSES = 5
total_number_rockets = 0
total_number_factories = 0
total_number_enemies = 0
non_worker_in_rocket = {}
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, 0, 1, -1]

def flood_fill(currentx, currenty, color):
	component[(currentx, currenty)] = color
	
	for c in range(8):
		newx, newy = currentx + di[c], currenty + dj[c]
		if newx >= 0 and newx <= marsHeight and newy >= 0 and newy <= marsWidth:
			if (newx, newy) not in component:
				temp_location = bc.MapLocation(bc.Planet.Mars, newx, newy)
				if marsMap.is_passable_terrain_at(temp_location):
					locations.append((newx, newy))
					flood_fill(newx, newy, color)
	
def find_free_locations_in_Mars():
	component_number = 0
	for i in range(marsHeight+1):
		for j in range(marsWidth+1):
			if (i, j) not in component:
				temp_location = bc.MapLocation(bc.Planet.Mars, i, j)
				try:
					if marsMap.is_passable_terrain_at(temp_location):
						#print('found free location on mars!')
						locations.append((i, j))
						flood_fill(i, j, component_number)
						component_number += 1
						
				except Exception as e:
					print(i, j)
					print('Error:', e)
					# use this to show where the error was
					traceback.print_exc()
		
# motherfucking thing does not work
# I have to binary search to find the dimensions of the map?

class GeneralActions(object):

	def preprocess(unit):
		return len(gc.sense_nearby_units_by_team(unit.location.map_location(), unit.vision_range, enemy_team))

	def move_bitch(unit, place, moveType):
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
				break
			
	def load_unit(unit):
		if gc.round() < data["Earth"]["second_phase"]["threshold"]:
			return
	
		# possible improvement: go into the most crowded garrison
		nearby = gc.sense_nearby_units_by_type(unit.location.map_location(), 2, bc.UnitType.Rocket)
		for other in nearby:
			if gc.can_load(other.id, unit.id):
				gc.load(other.id, unit.id)
				
				if unit.unit_type != bc.UnitType.Worker:
					if other.id in non_worker_in_rocket:
						non_worker_in_rocket[other.id] += 1
					else:
						non_worker_in_rocket[other.id] = 1
				break
				
	def move_towards_rocket(unit):
		if not gc.is_move_ready(unit.id):
			return
	
		location = unit.location.map_location()
		
		best_dir = directions[0]
		closest_distance = 100000
		nearby = gc.sense_nearby_units_by_type(location, unit.vision_range, bc.UnitType.Rocket)
		
		for other in nearby:
			other_location = other.location.map_location()
			current_distance = location.distance_squared_to(other_location)
			if current_distance < closest_distance:
				closest_distance = current_distance
				best_dir = location.direction_to(other_location)
		
		curr_idx = 8
		for i in range(8):
			if directions[i] == best_dir:
				curr_idx = i
				break
				
		for i in range(4):
			temp_idx = (curr_idx + i + 9)%9
			if gc.can_move(unit.id, directions[temp_idx]):
				gc.move_robot(unit.id, directions[temp_idx])
				return
			
			temp_idx = (curr_idx - i + 9)%9
			if gc.can_move(unit.id, directions[temp_idx]):
				gc.move_robot(unit.id, directions[temp_idx])
				return
		
	
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

class WorkerClass(object):

	def harvest_karbonite(unit):
		for dir in directions:
			if gc.can_harvest(unit.id, dir):
				#print('harvested karbonite!')
				gc.harvest(unit.id, dir)
				break
		
	def build_blueprint(unit, building_type):
	
		global total_number_rockets
		global total_number_factories
	
		for dir in directions:
			if gc.karbonite() >= building_type.blueprint_cost():
				if gc.can_blueprint(unit.id, building_type, dir):
					gc.blueprint(unit.id, building_type, dir)
					if building_type == bc.UnitType.Rocket:
						total_number_rockets += 1
					if building_type == bc.UnitType.Factory:
						total_number_factories += 1
			
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
		for dir in directions:
			if gc.can_replicate(unit.id, dir):
				gc.replicate(unit.id, dir)
				break
			
	def complete_build(unit, building_type):
		nearby = gc.sense_nearby_units_by_type(unit.location.map_location(), 2, building_type)
		for other in nearby:
			if gc.can_build(unit.id, other.id) and not other.structure_is_built():
				gc.build(unit.id, other.id)
				break

class MageClass(object):
	def blink_attack_mars(unit):
		if not gc.is_blink_ready(unit.id):
			return
		if bc.ResearchInfo().get_level(bc.UnitType.Mage) < 4:
			return
			
		location = unit.location
			
		possible_targets = sense_nearby_units_by_team(location.map_location(), 2, enemy_team)
		if len(possible_targets) > 2:
			return
			
		for guess in range(NUMBER_OF_GUESSES):
			i = random.randint(0, marsHeight-1)
			j = random.randint(0, marsWidth-1)
			
			try:
				temp_location = bc.MapLocation(bc.Planet.Mars, i, j)
				if gc.can_blink(unit.id, temp_location):
					gc.blink(unit.id, temp_location)
					return
					
			except Exception as e:
				print('Error:', e)
				# use this to show where the error was
				traceback.print_exc()

	def blink_attack_earth(unit):
		if not gc.is_blink_ready(unit.id):
			return
		if bc.ResearchInfo().get_level(bc.UnitType.Mage) < 4:
			return
			
		location = unit.location
		
		possible_targets = sense_nearby_units_by_team(location.map_location(), 2, enemy_team)
		if len(possible_targets) > 2:
			return
				
		for guess in range(NUMBER_OF_GUESSES):
			i = random.randint(0, earthHeight-1)
			j = random.randint(0, earthWidth-1)
			
			try:
				temp_location = bc.MapLocation(bc.Planet.Earth, i, j)
				if gc.can_blink(unit.id, temp_location):
					gc.blink(unit.id, temp_location)
					return
					
			except Exception as e:
				print('Error:', e)
				# use this to show where the error was
				traceback.print_exc()
				
class HealerClass(object):

	def heal_bitch(unit):
		if not gc.is_heal_ready(unit.id):
			return
			
		location = unit.location
		nearby = gc.sense_nearby_units_by_team(location.map_location(), unit.attack_range(), my_team)
		for other in nearby:
			if gc.can_heal(unit.id, other.id):
				# print('healed a friend!')
				gc.heal(unit.id, other.id)
				return
			
	def overcharge_attack(unit):
		if not gc.is_overcharge_ready(unit.id):
			return
		if bc.ResearchInfo().get_level(bc.UnitType.Healer) < 3:
			return
			
		location = unit.location
		
		possible_targets = sense_nearby_units_by_team(location.map_location(), unit.ability_range(), my_team)
		for other in possible_targets:
			if gc.can_heal(unit.id, other.id):
				gc.heal(unit.id, other.id)
				return
		
class RangerClass(object):

	def snipe_attack_mars(unit):
		if unit.ranger_is_sniping():
			return
		if not gc.is_begin_snipe_ready(unit.id):
			return
		if bc.ResearchInfo().get_level(bc.UnitType.Ranger) < 3:
			return
			
		for guess in range(NUMBER_OF_GUESSES):
			i = random.randint(0, marsHeight-1)
			j = random.randint(0, marsWidth-1)
			
			try:
				temp_location = bc.MapLocation(bc.Planet.Mars, i, j)
				if gc.can_begin_snipe(unit.id, temp_location):
					gc.begin_snipe(unit.id, temp_location)
					return
					
			except Exception as e:
				print('Error:', e)
				# use this to show where the error was
				traceback.print_exc()

	def snipe_attack_earth(unit):
		if unit.ranger_is_sniping():
			return
		if not gc.is_begin_snipe_ready(unit.id):
			return
		if bc.ResearchInfo().get_level(bc.UnitType.Ranger) < 3:
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
				
		for guess in range(NUMBER_OF_GUESSES):
			i = random.randint(0, earthHeight-1)
			j = random.randint(0, earthWidth-1)
			
			try:
				temp_location = bc.MapLocation(bc.Planet.Earth, i, j)
				if gc.can_begin_snipe(unit.id, temp_location):
					gc.begin_snipe(unit.id, temp_location)
					return
					
			except Exception as e:
				print('Error:', e)
				# use this to show where the error was
				traceback.print_exc()
	
class KnightClass(object):

	def javelin_attack(unit):
		if not gc.is_javelin_ready(unit.id):
			return
		if bc.ResearchInfo().get_level(bc.UnitType.Knight) < 3:
			return
			
		location = unit.location
		
		possible_targets = sense_nearby_units_by_team(location.map_location(), unit.ability_range(), enemy_team)
		for other in possible_targets:
			if gc.can_javelin(unit.id, other.id):
				gc.javelin(unit.id, other.id)
				return
		
class RocketClass(object):

	def get_free_location(unit):
		for t in range(NUMBER_OF_GUESSES):
			return_value = random.choice(locations)
			if (component[return_value] in color_chosen) and (t < NUMBER_OF_GUESSES-1):
				continue
			color_chosen.append(component[return_value])
			return bc.MapLocation(bc.Planet.Mars, return_value[0], return_value[1])

	def launch_rocket(unit):
		global total_number_rockets
		
		if gc.round() < data["Earth"]["second_phase"]["threshold"]:
			return
	
		garrison = unit.structure_garrison()
		
		if unit.id not in non_worker_in_rocket:
			return
		if non_worker_in_rocket[unit.id] < 2:
			return
		
		available_prob = launch_probability[len(garrison)]
		if random.random() < available_prob:
			#print('prepare for launch')
			free_loc = RocketClass.get_free_location(unit)
			
			if gc.can_launch_rocket(unit.id, free_loc):
				#print('launched rocket!')
				#update_team_array(free_loc)
				gc.launch_rocket(unit.id, free_loc)
				total_number_rockets -= 1
				
	def unload_rocket(unit):
		garrison = unit.structure_garrison()
		if len(garrison) > 0:
			for d in directions:
				if gc.can_unload(unit.id, d):
					#print('unloaded a poulla!')
					gc.unload(unit.id, d)
		#else:
			#gc.disintegrate_unit(unit.id)

class FactoryClass(object):

	def unload_factory(unit):
		garrison = unit.structure_garrison()
		if len(garrison) > 0:
			for d in directions:
				if gc.can_unload(unit.id, d):
					#print('unloaded a poulla!')
					gc.unload(unit.id, d)
			
	def produce_unit(unit, product_type):			
		if gc.can_produce_robot(unit.id, product_type):
			gc.produce_robot(unit.id, product_type)
			#print('produced a poulla!')
			
find_free_locations_in_Mars()
	
while True:
    # We only support Python 3, which means brackets around print()
	print('pyround:', gc.round(), 'time left:', gc.get_time_left_ms(), 'ms')
	
	try:
		for current_unit in gc.my_units():
			
			if current_unit.location.is_in_space() or current_unit.location.is_in_garrison():
				continue
				
	############  MARS  ###########
			
			elif current_unit.location.is_on_planet(bc.Planet.Mars):
				if current_unit.unit_type == bc.UnitType.Worker:
					p = random.random()
					if p < data["Mars"]["worker_harvest"]:
						WorkerClass.harvest_karbonite(current_unit)
						
					elif p < data["Mars"]["worker_replicate"]:
						WorkerClass.replicate_worker(current_unit)
					
					GeneralActions.attack_bitch(current_unit, p, "Mars", "worker_attack")	
					GeneralActions.move_bitch(current_unit, "Mars", "worker_move")
					
				if current_unit.unit_type == bc.UnitType.Knight:
					p = random.random()
					if p < data["Mars"]["knight_javelin"]:
						KnightClass.javelin_attack(current_unit)
					
					GeneralActions.attack_bitch(current_unit, p, "Mars", "knight_attack")	
					GeneralActions.move_bitch(current_unit, "Mars", "knight_move")
				
				if current_unit.unit_type == bc.UnitType.Mage:
					p = random.random()
					if p < data["Mars"]["mage_blink"]:
						MageClass.blink_attack_mars(current_unit)
					
					GeneralActions.attack_bitch(current_unit, p, "Mars", "mage_attack")	
					GeneralActions.move_bitch(current_unit, "Mars", "mage_move")
				
				if current_unit.unit_type == bc.UnitType.Ranger:
					p = random.random()
					if p < data["Mars"]["ranger_snipe"]:
						RangerClass.snipe_attack_mars(current_unit)
					
					GeneralActions.attack_bitch(current_unit, p, "Mars", "ranger_attack")	
					GeneralActions.move_bitch(current_unit, "Mars", "ranger_move")
				
				if current_unit.unit_type == bc.UnitType.Healer:
					p = random.random()
					if p < data["Mars"]["healer_overcharge"]:
						HealerClass.overcharge_attack(current_unit)
					
					HealerClass.heal_bitch(current_unit)	
					GeneralActions.move_bitch(current_unit, "Mars", "healer_move")
					
				if current_unit.unit_type == bc.UnitType.Rocket:
					RocketClass.unload_rocket(current_unit)
					
					
	############  EARTH  ###########
				
			elif current_unit.location.is_on_planet(bc.Planet.Earth):
			
				phase_number = "third_phase"
				if gc.round() <= data["Earth"]["first_phase"]["threshold"]:
					phase_number = "first_phase"
				elif gc.round() <= data["Earth"]["second_phase"]["threshold"]:
					phase_number = "second_phase"
					
				if 100 <= gc.round() and gc.round() <= 169 and total_number_factories < 3:
					phase_number = "emergency_factory"
				
				if phase_number == "second_phase" and total_number_rockets < 4:
					phase_number = "emergency_rocket"
					print("EMERGENCY MODE")
					
				if phase_number == "first_phase" and (total_number_enemies/len(gc.my_units()) >= 0.6):
					phase_number = "emergency_attack"
					
			
				if current_unit.unit_type == bc.UnitType.Worker:
					total_number_enemies += GeneralActions.preprocess(current_unit)
					WorkerClass.complete_build(current_unit, bc.UnitType.Rocket)
					WorkerClass.complete_build(current_unit, bc.UnitType.Factory)
						
					GeneralActions.load_unit(current_unit)
					
					p = random.random()
					if p < data["Earth"][phase_number]["worker_harvest"]:
						WorkerClass.harvest_karbonite(current_unit)
						
					elif p < data["Earth"][phase_number]["worker_replicate"]:
						WorkerClass.replicate_worker(current_unit)
						
					elif p < data["Earth"][phase_number]["worker_blueprint_factory"]:
						WorkerClass.build_blueprint(current_unit, bc.UnitType.Factory)
						
					elif p < data["Earth"][phase_number]["worker_blueprint_rocket"]:
						WorkerClass.build_blueprint(current_unit, bc.UnitType.Rocket)

					elif p < data["Earth"][phase_number]["worker_repair"]:
						WorkerClass.repair(current_unit)
						
					GeneralActions.attack_bitch(current_unit, p, "Earth", "worker_attack")	
					GeneralActions.move_bitch(current_unit, "Earth", "worker_move")
					
				if current_unit.unit_type == bc.UnitType.Knight:
					total_number_enemies += GeneralActions.preprocess(current_unit)
					GeneralActions.load_unit(current_unit)
					GeneralActions.move_towards_rocket(current_unit)
				
					p = random.random()
					if p < data["Earth"]["knight_javelin"]:
						KnightClass.javelin_attack(current_unit)
						
					GeneralActions.attack_bitch(current_unit, p, "Earth", "knight_attack")	
					GeneralActions.move_bitch(current_unit, "Earth", "knight_move")
				
				if current_unit.unit_type == bc.UnitType.Mage:
					total_number_enemies += GeneralActions.preprocess(current_unit)
					GeneralActions.load_unit(current_unit)
					GeneralActions.move_towards_rocket(current_unit)
				
					p = random.random()
					if p < data["Earth"]["mage_blink"]:
						MageClass.blink_attack_earth(current_unit)
					
					GeneralActions.attack_bitch(current_unit, p, "Earth", "mage_attack")	
					GeneralActions.move_bitch(current_unit, "Earth", "mage_move")
				
				if current_unit.unit_type == bc.UnitType.Ranger:
					total_number_enemies += GeneralActions.preprocess(current_unit)
					GeneralActions.load_unit(current_unit)
					GeneralActions.move_towards_rocket(current_unit)
				
					p = random.random()
					if p < data["Earth"]["ranger_snipe"]:
						RangerClass.snipe_attack_earth(current_unit)
					
					GeneralActions.attack_bitch(current_unit, p, "Earth", "ranger_attack")	
					GeneralActions.move_bitch(current_unit, "Earth", "ranger_move")
				
				if current_unit.unit_type == bc.UnitType.Healer:
					total_number_enemies += GeneralActions.preprocess(current_unit)
					GeneralActions.load_unit(current_unit)
					GeneralActions.move_towards_rocket(current_unit)
				
					p = random.random()
					if p < data["Earth"]["healer_overcharge"]:
						HealerClass.overcharge_attack(current_unit)
					
					HealerClass.heal_bitch(current_unit)	
					GeneralActions.move_bitch(current_unit, "Earth", "healer_move")
				
				if current_unit.unit_type == bc.UnitType.Factory:
					FactoryClass.unload_factory(current_unit)
					if current_unit.is_factory_producing():
						continue
					
					p = random.random()
					if p < data["Earth"][phase_number]["produce_worker"]:
						FactoryClass.produce_unit(current_unit, bc.UnitType.Worker)
						
					elif p < data["Earth"][phase_number]["produce_knight"]:
						FactoryClass.produce_unit(current_unit, bc.UnitType.Knight)
					
					elif p < data["Earth"][phase_number]["produce_healer"]:
						FactoryClass.produce_unit(current_unit, bc.UnitType.Healer)
					
					elif p < data["Earth"][phase_number]["produce_mage"]:
						FactoryClass.produce_unit(current_unit, bc.UnitType.Mage)
						
					elif p < data["Earth"][phase_number]["produce_ranger"]:
						FactoryClass.produce_unit(current_unit, bc.UnitType.Ranger)
					
				if current_unit.unit_type == bc.UnitType.Rocket:
					p = random.random()
					if p < data["Earth"][phase_number]["rocket_launch"]:
						RocketClass.launch_rocket(current_unit)
						
				if phase_number == "third_phase":
					if total_number_rockets == 0:
						total_number_rockets = -1
						data["Earth"][phase_number]["worker_harvest"] = 0.95
						data["Earth"][phase_number]["worker_replicate"] = 1.0
						data["Earth"][phase_number]["worker_blueprint_factory"] = 0.0
						data["Earth"][phase_number]["worker_blueprint_rocket"] = 0.0
						data["Earth"][phase_number]["worker_repair"] = 0.0
						data["Earth"][phase_number]["worker_attack"] = 0.0
						data["Earth"][phase_number]["worker_move"] = 1.0
						
			
						data["Earth"][phase_number]["produce_worker"] = 0.05
						data["Earth"][phase_number]["produce_knight"] = 0.0
						data["Earth"][phase_number]["produce_healer"] = 0.0
						data["Earth"][phase_number]["produce_mage"] = 0.0
						data["Earth"][phase_number]["produce_ranger"] = 0.0
						data["Earth"][phase_number]["rocket_launch"] = 0.69
				
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
