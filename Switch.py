# Prompting to switch
def will_switch():
    response = ""
    
    while response.lower() not in ["y", "n", "yes", "no"]:
        response = input("Would you like to switch? (y/n) ")
    if response == "n" or response == "no":
        return False
    elif response == "y" or response == "yes":
        return True



    