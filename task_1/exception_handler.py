from colorama import Fore, Style
from functools import wraps

def handle_exceptions(func):
    """
    A decorator to handle exceptions that may occur during the execution of the decorated function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function with exception handling.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PermissionError:
            print(f"{Fore.RED} [ERROR] Permission denied while accessing '{args[0]}'{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED} [ERROR] An error occurred while accessing '{args[0]}': {e}{Style.RESET_ALL}")
    return wrapper
