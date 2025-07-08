import Switch
import Initial_Door
import Again
import Random_Doors
import Montys_Door
import Visuals
from Montys_Door import doors
from Visuals import correct_door
from Visuals import wrong_door


total_played = 0
total_won = 0



# Chosing the inital chose and seeing what Monty revealed.
global first
first = Initial_Door.initial_door() + 1
monty_door = Montys_Door.monty_door(first, doors) + 1

print(f"\nYou chose door {first}. You don't know what's behind it.")
print(f"Monty revealed that door {monty_door} is wrong.")
show_doors = Visuals.show_doors(monty_door, first)
print(show_doors)


# Finding what door is left to switch with
doors_left = [1, 2, 3]
doors_left.remove(first)
doors_left.remove(monty_door)
door_left = doors_left[0]
print(f"So door {door_left} is remaining.")


# Switching
switch = Switch.will_switch()

if switch == True:
    if doors[door_left - 1] == "correct":
        print(correct_door)
        print("Win! Good job switching.")
        total_won += 1
    else:
        print(wrong_door)
        print("Lose. Better luck next time.")
elif switch == False:
    if doors[first_door] == "correct":
        print(correct_door)
        print("Your original pick paid off! Win!")
        total_won += 1
    else:
        print(wrong_door)
        print("Lose. Shoulda switched.")
        
        
# Calculates win ratio
total_played += 1
win_ratio = (total_won / total_played * 100)
win_rate = print(f"{win_ratio:.2f}% Win-Lose\n")




# Asks to play again

while total_played >= 1:
    again = Again.play_again()
    
    if again == True:
        # Generates new random doors for next round
        doors = Random_Doors.get_random_doors()
        
        # Chosing the inital chose and seeing what Monty revealed.
        first = Initial_Door.initial_door() + 1
        monty_door = Montys_Door.monty_door(first, doors) + 1

        print(f"You chose door {first}. You don't know what's behind it.")
        print(f"Monty revealed that door {monty_door} is wrong.")


        # Finding what door is left to switch with
        doors_left = [1, 2, 3]
        doors_left.remove(first)
        doors_left.remove(monty_door)
        door_left = doors_left[0]
        print(f"So door {door_left} is remaining.")


        # Switching
        switch = Switch.will_switch()

        if switch == True:
            if doors[door_left - 1] == "correct":
                print(correct_door)
                print("Win! Good job switching.")
                total_won += 1
            else:
                print(wrong_door)
                print("Lose. Better luck next time.")
        elif switch == False:
            if doors[first_door] == "correct":
                print(correct_door)
                print("Your original pick paid off! Win!")
                total_won += 1
            else:
                print(wrong_door)
                print("Lose. Shoulda switched.")
                
                
        # Calculates win ratio
        total_played += 1
        win_ratio = float(total_won / total_played * 100)
        win_rate = print(f"{win_ratio:.2f}% Win-Lose\n")


    else:
        print("Terminating...")
        break










