# Returns the index of the door initially chosen
def initial_door():
    first_door = 0
    
    while first_door != 1 and first_door != 2 and first_door != 3:
        first_door = int(input("Which door would you like to first pick? (1-3) "))
        
    if first_door == 1:
        return 0
    elif first_door == 2:
        return 1
    elif first_door == 3:
        return 2

    
    
    
    
    
    
    
    
    
    
    
    



# ACII door art

closed_doors = (r"""
 _______   _______   _______
|       | |       | |       |
|  ___  | |  ___  | |  ___  |
| |   | | | |   | | | |   | |
| | o | | | | o | | | | o | |
| |___| | | |___| | | |___| |
|_______| |_______| |_______|
""")

wrong_door = (r"""
 _______
|       |
|       |
|       |
|       |
|       |
|_______|
""")

correct_door = (r"""
 _______
|       |
|  /\_/\|
| ( o.o ) 
| > ^ < |
|       |
|_______|
""")