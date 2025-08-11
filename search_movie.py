from typing import Optional

from json_manager import load_movies
from movie import Movie
from search_manager import (
    SearchType,
    prompt_search_type,
    search_movies,
    display_results,
    prompt_movie_choice
)


MENU_HEADER = "- = - Movie Search - = -"
MENU_SUBHEADER = "What would you like to search for?"
PROMPT_TEXT = "Which movie do you want to view?"


def search_movie(file_path: str) -> None:
    movies = load_movies(file_path)
    if not movies:
        print("There are no movies in your collection. Returning to the main menu.\n")
        return
    while True:
        search_type = prompt_search_type(MENU_HEADER, MENU_SUBHEADER)
        if search_type is None:
            print("Returning to the main menu.\n")
            return
        if search_type == "invalid":
            continue
        if not isinstance(search_type, (type(None), type)) and not isinstance(search_type, object):
            continue
        if not isinstance(search_type, SearchType):
            continue
        search_term = input("Please enter your search term: ").strip()
        results = sorted(
            search_movies(movies, search_type, search_term),
            key=lambda m: (m.release_year, m.title),
        )
        if not results:
            print("\nNo movies were found. Restarting the search.")
            continue
        display_results(results, MENU_HEADER)
        choice = prompt_movie_choice(results, PROMPT_TEXT)
        if choice == "restart" or choice is None:
            continue
        if isinstance(choice, Movie):
            choice.print()
        new_search = input("\nWould you like to start a new search (Y/N)? ").strip().lower()
        if new_search in ("y", "yes"):
            print("Starting a new search.")
            continue
        print("Returning to the main menu.\n")
        break
