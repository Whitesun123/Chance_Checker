import os

def clear():
    """ Clears the console """
    
    os.system('cls' if os.name == 'nt' else 'clear')