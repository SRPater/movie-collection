import os
import sys

from add_movie import add_movie
from search_movie import search_movie


BASE_DIR = os.getcwd()
FILE_PATH = os.path.join(BASE_DIR, "collection/movies.json")


def main():
    while True:
        print("┌──────────────────────────────┐")
        print("│ - = - Movie Collection - = - │")
        print("│  What would you like to do?  │")
        print("╞══════════════════════════════╡")
        print("│ 1. Search for a movie        │")
        print("│ 2. Add a new movie           │")
        print("│ 3. Edit a movie              │")
        print("│ 4. Delete a movie            │")
        print("│ 5. Exit the Movie Collection │")
        print("└──────────────────────────────┘")
        
        try:
            main_menu_choice = int(input("\nMake your selection please (1-5): ").strip())
        except ValueError:
            print("Invalid choice. Please choose a number.\n")
        
        match main_menu_choice:
            case 1:
                search_movie(FILE_PATH)
            case 2:
                add_movie(FILE_PATH)
            case 3:
                print("You've chosen to edit a movie.\n")
            case 4:
                print("You've chosen to delete a movie.\n")
            case 5:
                print("Exiting the Movie Collection. See you next time!\n")
                sys.exit(0)
            case _:
                print("Invalid choice. Please choose a number from 1-5.\n")


if __name__ == "__main__":
    main()
