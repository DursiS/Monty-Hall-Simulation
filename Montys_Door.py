import random
import Random_Doors
from Random_Doors import doors

# Returns the number of the door Monty chose 
def monty_door(first, doors):
    
    first_door = first - 1
    doors_left = [0, 1, 2]
    doors_left.remove(first_door)
    num = random.randint(0,1)
    
    # Returns the index number of the remaining doors, in relation to doors list.
    first_remaining = doors_left[0]
    second_remaining = doors_left[1]
    random_remaining = doors_left[num]
    
    # Returns the index number to the door Monty chose, in relation to doors list.
    if doors[first_remaining] == "correct" and doors[second_remaining] == "wrong":
        return second_remaining
    elif doors[first_remaining] == "wrong" and doors[second_remaining] == "correct":
        return first_remaining
    else:
        return random_remaining