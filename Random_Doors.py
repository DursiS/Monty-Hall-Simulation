import random
global doors

# Generates what is behind each door
def get_random_doors():
    correct_or_not = ["correct", "wrong", "wrong"]
    doors = []
        
    for i in range(0,3):
        
        # Chooses a random door and finds its index
        random_door = random.choice(correct_or_not)
        random_door_index = correct_or_not.index(random_door)
        
        # Adds that random door to the empty list and removes it from the original to not get chosen again
        doors.append(random_door)
        correct_or_not.pop(random_door_index)
    return doors
    
doors = get_random_doors()