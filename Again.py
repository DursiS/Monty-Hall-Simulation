# Asks to play again, returns a boolean
def play_again():
    play_again = ""
    
    while play_again.lower() not in ["y", "n", "yes", "no"]:
        play_again = input("Would you like to play again? (y/n) ")
        
    if play_again == "n" or play_again == "no":
        return False
    elif play_again == "y" or play_again == "yes":
        return True