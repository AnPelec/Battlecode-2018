import battlecode as bc
import random
import sys
import traceback
import time

import os
print(os.getcwd())

# A GameController is the main type that you talk to the game with.
# Its constructor will connect to a running game.
op = bc.OrbitPattern()
directions = list(bc.Direction)

print("pystarted")

# It's a good idea to try to keep your bots deterministic, to make debugging easier.
# determinism isn't required, but it means that the same things will happen in every thing you run,
# aside from turns taking slightly different amounts of time due to noise.
random.seed(6137)

# let's start off with some research!
# we can queue as much as we want.

my_team = gc.team()
earth_flood_round = 750

class RocketLaunch(object):
	
	def __init__(self):
		arrival_time = [i for i in range(earth_flood_round)]
		for current_round in range(1, earth_flood_round):
			arrival_time[i] += op.duration(i)
		
		best_launch_time = [i for i in range(earth_flood_round)]
		for current_round in range(earth_flood_round-2, 0, -1):
			if arrival_time[best_launch_time[current_round+1]] < arrival_time[current_round]:
				best_launch_time[current_round] = best_launch_time[current_round+1]
			else:
				best_launch_time[current_round] = current_round
				
	def get_launch_time(self, round):
		return best_launch_time(round)
