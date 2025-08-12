from typing import Optional

from core.movie import Movie
from core.search_manager import (
    run_search_loop
)


MENU_HEADER = "- = - Movie Search - = -"
MENU_SUBHEADER = "What would you like to search for?"
PROMPT_TEXT = "Which movie do you want to view?"


def on_search_choice(movie: Movie, movies: list[Movie], _file_path: str) -> bool:
    movie.print()
    new_search = input("\nWould you like to start a new search? (Y/N) ").strip().lower()
    return new_search in ("y", "yes")

def search_movie(file_path: str) -> None:
    run_search_loop(file_path, MENU_HEADER, MENU_SUBHEADER, PROMPT_TEXT, on_search_choice)
