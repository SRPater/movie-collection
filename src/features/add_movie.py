from datetime import datetime
from typing import List

from core.input_manager import (
    get_valid_title,
    get_valid_release_year,
    get_director,
    get_cast,
    get_summary
)
from core.json_manager import load_movies, save_movies
from core.movie import Movie


def add_movie(file_path: str) -> None:
    existing_movies = load_movies(file_path)
    print("\nWe need to know some information about a movie before we can add it to the collection.")
    while True:
        title = get_valid_title(existing_movies)
        release_year = get_valid_release_year()
        director = get_director()
        cast = get_cast()
        summary = get_summary()
        new_movie = Movie(title, release_year, director, cast, summary)
        existing_movies.append(new_movie)
        try:
            save_movies(file_path, existing_movies)
        except Exception as e:
            print(f"\nSomething went wrong while saving: {e}")
            return
        print(f"Succesfully added {new_movie.title} to the collection.")
        new_movie.print()
        add_more_input = input("\nWould you like to add another movie (Y/N)? ").strip().lower()
        if add_more_input not in ("y", "yes"):
            print("Returning to the main menu.\n")
            break
        print("Alright, let's add another one.\n")
