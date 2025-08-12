from typing import List, Optional

from core.input_manager import (
    get_valid_title,
    get_valid_release_year,
    get_director,
    get_cast,
    get_summary
)
from core.json_manager import save_movies
from core.movie import Movie
from core.search_manager import run_search_loop


MENU_HEADER = "- = - Edit Movie - = -"
MENU_SUBHEADER = "How would you like to find a movie to edit?"
PROMPT_TEXT = "Which movie do you want to edit?"


def on_edit_choice(movie: Movie, movies: List[Movie], file_path: str) -> bool:
    new_title = get_valid_title(movies, movie.title)
    new_release_year = get_valid_release_year(movie.release_year)
    new_director = get_director(movie.director)
    new_cast = get_cast(movie.cast)
    new_summary = get_summary(movie.summary)
    new_movie = Movie(new_title, new_release_year, new_director, new_cast, new_summary, movie.id)
    movies.remove(movie)
    movies.append(new_movie)
    try:
        save_movies(file_path, movies)
    except Exception as e:
        print(f"\nSomething went wrong while saving: {e}")
        return False
    print(f"\nSuccesfully edited {new_movie.title}.")
    new_movie.print()
    edit_more = input("\nWould you like to edit another movie? (Y/N) ").strip().lower()
    return edit_more in ("y", "yes")


def edit_movie(file_path: str) -> None:
    run_search_loop(file_path, MENU_HEADER, MENU_SUBHEADER, PROMPT_TEXT, on_edit_choice)
