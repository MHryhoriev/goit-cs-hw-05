from input_validator import validate_input_path
from file_handler import list_files_and_directories
from structure_printer import print_final_structure
from colorama import Fore, Style
import asyncio

async def main():
    source_path, destination_path = validate_input_path()

    print(f"\n{Fore.YELLOW}Structure of source directory:{Style.RESET_ALL}")
    await list_files_and_directories(source_path, destination_path)

    print(f"\n{Fore.YELLOW}Structure of destination directory:{Style.RESET_ALL}")
    await print_final_structure(destination_path)

if __name__ == "__main__":
    asyncio.run(main())