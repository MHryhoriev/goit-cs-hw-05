import shutil
import asyncio
from colorama import Fore, Style
from pathlib import Path
from exception_handler import handle_exceptions

@handle_exceptions
async def list_files_and_directories(source_directory_path: Path, destination_directory_path: Path, depth: int = 0) -> None:
    """
    Recursively lists files and directories in the source directory and copies files to a destination directory
    organized by their file extensions.

    Args:
        source_directory_path (Path): The path to the source directory to list files from.
        destination_directory_path (Path): The path to the destination directory to copy files to.
        depth (int): The current depth in the directory structure (used for formatting output). Defaults to 0.
    
    Returns:
        None
    """
    if depth == 0:
        print(f"{Fore.BLUE} {source_directory_path.name}/{Style.RESET_ALL}")

    tasks = []

    for path in source_directory_path.iterdir():
        indent = "  " * (depth + 1)
        if path.is_file():
            print(f"{indent}{Fore.GREEN} {path.name}{Style.RESET_ALL}")
            tasks.append(copy_file_to_destination(path, destination_directory_path))
        elif path.is_dir():
            print(f"{indent}{Fore.BLUE} {path.name}/")
            tasks.append(list_files_and_directories(path, destination_directory_path, depth + 1))
    
    await asyncio.gather(*tasks)

@handle_exceptions
async def copy_file_to_destination(path: Path, destination_directory_path: Path) -> None:
    """
    Copies a file to a destination directory, creating a subdirectory based on the file's extension.

    Args:
        path (Path): The path of the file to be copied.
        destination_directory_path (Path): The path of the destination directory where the file will be copied.
    
    Returns:
        None
    """
    file_extension = path.suffix[1:]
    if file_extension:
        new_dir = destination_directory_path / file_extension
        new_dir.mkdir(parents=True, exist_ok=True)
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, shutil.copy2, path, new_dir / path.name)
