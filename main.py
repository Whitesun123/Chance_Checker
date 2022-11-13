# Rich imports
from rich.console import Console
console = Console()
from rich import print
# Cog imports
from cogs.titlename import titleNameStart
from cogs.get_time import get_time
from cogs.guess import Guess
from cogs.clear import clear
# Other imports
from time import sleep
import os
from InquirerPy import inquirer

try:
    
    @get_time   
    def main():
        """ Runs the main function """
        
        clear()
        titleNameStart()
        result = inquirer.confirm(message="Do you want to display a percentage graph at the end?:", default=True).execute()
        Guess.guesser(result)
        
    if __name__ == '__main__':
        main()
    
except Exception:
    console.print_exception(show_locals=False)