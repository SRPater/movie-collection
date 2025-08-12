from typing import List

from core.json_manager import save_movies
from core.movie import Movie
from core.search_manager import run_search_loop


MENU_HEADER = "- = - Delete Movie - = -"
MENU_SUBHEADER = "How would you like to search for a movie to delete?"
PROMPT_TEXT = "Which movie would you like to delete?"


def on_delete_choice(movie: Movie, movies: List[Movie], file_path: str) -> bool:
    certain_input = input(f"Are you sure you want to delete {movie.title} from the collection? (Y/N) ").strip().lower()
    if certain_input not in ("y", "yes"):
        return True
    movies.remove(movie)
    try:
        save_movies(file_path, movies)
    except Exception as e:
        print(f"\nSomething went wrong while saving: {e}")
        return False
    print(f"\nSuccesfully deleted {movie.title}.")
    delete_more = input("Would you like to delete another movie? (Y/N) ").strip().lower()
    return delete_more in ("y", "yes")


def delete_movie(file_path: str) -> None:
    run_search_loop(file_path, MENU_HEADER, MENU_SUBHEADER, PROMPT_TEXT, on_delete_choice)
