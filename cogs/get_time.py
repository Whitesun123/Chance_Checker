from time import perf_counter
from rich import print

def get_time(func):
    """ Get the runtime of any function

    Args:
        func (arg): Grabs the functions runtime
    """
    
    def wrapper(*args, **kwargs):
        """ Gets the start and end time of the function then prints the end time """
        
        start_time = perf_counter()
        
        func(*args, **kwargs)
        
        end_time = perf_counter()
        
        total_time = round(end_time - start_time, 2)
        
        print("\nFunction took " + str(total_time) + " seconds")
        
    return wrapper