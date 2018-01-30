import battlecode as bc
import random
import sys
import traceback
import worker

print("pystarting")

# A GameController is the main type that you talk to the game with.
# Its constructor will connect to a running game.
gc = bc.GameController()
directions = list(bc.Direction)

print("pystarted")

# It's a good idea to try to keep your bots deterministic, to make debugging easier.
# determinism isn't required, but it means that the same things will happen in every thing you run,
# aside from turns taking slightly different amounts of time due to noise.
random.seed(6137)

while True:
    # We only support Python 3, which means brackets around print()
    print('pyround:', gc.round())
	
	for current_unit in gc.my_units():
		if current_unit.unit_type == UnitType.Worker:
		
		if current_unit.unit_type == UnitType.Knight:
		
		if current_unit.unit_type == UnitType.Mage:
		
		if current_unit.unit_type == UnitType.Ranger:
		
		if current_unit.unit_type == UnitType.Healet:
		
		if current_unit.unit_type == UnitType.Factory:
		
		if current_unit.unit_type == UnitType.Rocket:

    # send the actions we've performed, and wait for our next turn.
    gc.next_turn()

    # these lines are not strictly necessary, but it helps make the logs make more sense.
    # it forces everything we've written this turn to be written to the manager.
    sys.stdout.flush()
    sys.stderr.flush()
