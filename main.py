import os
import sys
from typing import NoReturn

from add_movie import add_movie
from edit_movie import edit_movie
from search_movie import search_movie


BASE_DIR: str = os.path.dirname(__file__)
FILE_PATH: str = os.path.join(BASE_DIR, "collection/movies.json")
MENU: str = """┌──────────────────────────────┐
│ - = - Movie Collection - = - │
│  What would you like to do?  │
╞══════════════════════════════╡
│ 1. Search for a movie        │
│ 2. Add a new movie           │
│ 3. Edit a movie              │
│ 4. Delete a movie            │
│ 5. Exit the Movie Collection │
└──────────────────────────────┘
"""


def print_menu() -> None:
    print(MENU)


def main() -> NoReturn:
    while True:
        print_menu()
        try:
            main_menu_choice = int(input("Make your selection please (1-5): ").strip())
        except ValueError:
            print("Invalid choice. Please choose a number.\n")
            continue
        
        match main_menu_choice:
            case 1:
                search_movie(FILE_PATH)
            case 2:
                add_movie(FILE_PATH)
            case 3:
                edit_movie(FILE_PATH)
            case 4:
                print("You've chosen to delete a movie.\n")
            case 5:
                print("Exiting the Movie Collection. See you next time!\n")
                sys.exit(0)
            case _:
                print("Invalid choice. Please choose a number from 1-5.\n")


if __name__ == "__main__":
    main()
