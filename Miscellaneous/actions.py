import battlecode as bc
import random
import sys
import traceback

gc = bc.GameController()
my_team = gc.team()

# should we make it true or false, so we know what happened?
def unit_attack(unit):
	location = unit.location
    if location.is_on_map():
		nearby = gc.sense_nearby_units(location.map_location(), 2)
        for other in nearby:
			if other.team != my_team and gc.is_attack_ready(unit.id) and gc.can_attack(unit.id, other.id):
				print('attacked a thing!')
				gc.attack(unit.id, other.id)
				continue
				
def get_karbonite(unit):
	for dir in bc.Direction:
		if gc.can_harvest(unit.id, dir):
			print('harvested karbonite!')
			gc.harvest(unit.id, dir)
			continue
			
def unit_heal(unit):
	location = unit.location
	if location.is_on_map():
		nearby = gc.sense_nearby_units(location.map_location(), 2)
		for other in nearby:
			if other.team == my_team and gc.is_heal_ready(unit.id) and gc.can_heal(unit.id, other.id):
				print('healed a friend!')
				gc.heal(unit.id, other.id)
				continue
				
def move_and_expand(unit):

	best_dir = bc.Direction(0)
	less_units = 10

	location = unit.location
	for dir in bc.Direction:
		new_location = location.add(dir)
		if new_location.is_on_map():
			nearby_units = gc.sense_nearby_units_by_team(new_location.map_location(), 2, my_team)
			current_units = gc.sense_nearby_units(new_location.map_location(), 1)
			if nearby_units < less_units and gc.is_passable_terrain:
				less_units = nearby_units
				best_dir = dir
