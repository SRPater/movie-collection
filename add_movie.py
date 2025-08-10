from datetime import datetime
import json

from json_manager import json_to_movies
from movie import Movie, movie_to_dictionary


def add_movie(file_path):
    try:
        with open(file_path, "r") as file:
            json_data = json.load(file)
    except json.JSONDecodeError:
        json_data = {"movies": []}
    existing_movies = json_to_movies(json_data)
    print("\nWe need to know some information about a movie before we can add it to the collection.")
    title = input("What is the title of the movie? ").strip()
    if title == "":
        print("Please enter a title.")
        return add_movie(file_path)
    if len(title) > 100:
        print("A title can be no longer than 100 characters.")
        return add_movie(file_path)
    for movie in existing_movies:
        if movie.title.lower() == title.lower():
            print("A movie with that title already exists in your collection.")
            return add_movie(file_path)
    try:
        release_year = int(input("In what year was the movie released? ").strip())
    except ValueError:
        print("Please enter a number.")
        return add_movie(file_path)
    if release_year < 1900 or release_year > datetime.now().year:
        print(f"The release year must be between 1900 and {datetime.now().year}.")
        return add_movie(file_path)
    director = input("Who directed the movie? ").strip()
    cast_members = input("Who starred in this movie? Separate cast members with a comma. ").strip()
    cast = cast_members.split(",")
    summary = input("Give a short summary of the movie. ").strip()
    new_movie = Movie(title, release_year, director, cast, summary)
    movie_dict = movie_to_dictionary(new_movie)
    movies = json_data["movies"]
    movies.append(movie_dict)
    try:
        with open(file_path, "w") as json_file:
            json.dump({"movies": movies}, json_file)
    except Exception:
        print("\nSomething went wrong. Please try again.")
        return add_movie(file_path)
    print(f"Successfully added {new_movie.title} to the collection.")
    new_movie.print()
    add_more_input = input("\nWould you like to add another movie (Y/N)? ").strip()
    if add_more_input.lower() == "y" or add_more_input.lower() == "yes":
        print("Alright, let's add another one.\n")
        return add_movie(file_path)
    elif add_more_input.lower() == "n" or add_more_input.lower() == "no":
        print("Returning to main menu.\n")
    else:
        print("Invalid input. Returning to main menu.\n")
