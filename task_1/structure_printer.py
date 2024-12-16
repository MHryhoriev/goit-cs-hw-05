import asyncio
from colorama import Fore, Style
from pathlib import Path

async def print_final_structure(destination_directory_path: Path, depth: int = 0) -> None:
    """
    Recursively prints the structure of the destination directory, including 
    subdirectories and files, with indentation to indicate the depth.

    Args:
        destination_directory_path (Path): The path to the destination directory whose structure is to be printed.
        depth (int, optional): The current depth in the directory structure, used for indentation. Defaults to 0.

    Returns:
        None
    """
    tasks = []

    for path in destination_directory_path.iterdir():
        indent = "  " * depth
        if path.is_dir():
            print(f"{indent}{Fore.BLUE} {path.name}/")
            tasks.append(print_final_structure(path, depth + 1))
        elif path.is_file():
            print(f"{indent}{Fore.GREEN} {path.name}{Style.RESET_ALL}")

    await asyncio.gather(*tasks)