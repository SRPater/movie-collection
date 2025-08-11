from datetime import datetime
from typing import List

from json_manager import load_movies, save_movies
from movie import Movie


def get_valid_title(existing_movies: List[Movie]) -> str:
    while True:
        title = input("What is the title of the movie? ").strip()
        if not title:
            print("Please enter a title.")
        elif len(title) > 100:
            print("A title can not be longer than 100 characters.")
        elif any(m.title.lower() == title.lower() for m in existing_movies):
            print("A movie with that title already exists in your collection.")
        else:
            return title


def get_valid_release_year() -> int:
    current_year = datetime.now().year
    while True:
        try:
            year = int(input("In what year was the movie released? ").strip())
        except ValueError:
            print("Please enter a number.")
        if 1900 <= year <= current_year:
            return year
        print(f"The release year must be between 1900 and {current_year}.")


def add_movie(file_path: str) -> None:
    existing_movies = load_movies(file_path)
    print("\nWe need to know some information about a movie before we can add it to the collection.")
    title = get_valid_title(existing_movies)
    release_year = get_valid_release_year()
    director = input("Who directed the movie? ").strip()
    cast_input = input("Who starred in this movie? Separate cast members with a comma. ").strip()
    cast = [member.strip() for member in cast_input.split(",") if member.strip()]
    summary = input("Give a short summary of the movie. ").strip()
    new_movie = Movie(title, release_year, director, cast, summary)
    existing_movies.append(new_movie)
    try:
        save_movies(file_path, existing_movies)
    except Exception:
        print("\nSomething went wrong while saving. Please try again.")
        return
    print(f"Succesfully added {new_movie.title} to the collection.")
    new_movie.print()
    add_more_input = input("\nWould you like to add another movie (Y/N)? ").strip().lower()
    if add_more_input in ("y", "yes"):
        print("Alright, let's add another one.\n")
        add_movie(file_path)
    else:
        print("Returning to the main menu.\n")
