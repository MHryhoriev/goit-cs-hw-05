import sys
from colorama import Fore, Style
from pathlib import Path
from typing import Tuple

def validate_input_path() -> Tuple[Path, Path]:
    """
    Validates the command-line arguments provided for the source and destination directory paths.

    Returns:
        tuple: A tuple containing the validated source directory path (Path) and the destination directory 
               path (Path).
    
    Raises:
        SystemExit: If the number of arguments is incorrect, or if the source directory does not exist or is not a valid directory.
    """
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f"{Fore.RED} [ERROR] Usage: py main.py [/path/to/your/source_directory] [/path/to/your/destination_directory] {Style.RESET_ALL}")
        sys.exit(1)

    source_directory_path = Path(sys.argv[1])
    destination_directory_path = Path(sys.argv[2]) if len(sys.argv) == 3 else Path('./dist')

    if not source_directory_path.exists() or not source_directory_path.is_dir():
        print(f"{Fore.RED} [ERROR] Directory '{source_directory_path}' not found or is not a valid directory!{Style.RESET_ALL}")
        sys.exit(1)

    if len(sys.argv) == 2 and not destination_directory_path.exists():
        print(f"{Fore.YELLOW} [WARNING] Directory '{destination_directory_path}' does not exist. It will be created.{Style.RESET_ALL}")

    return source_directory_path, destination_directory_path
