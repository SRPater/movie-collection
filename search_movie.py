import json
from enum import Enum

from movie import Movie


class SearchType(Enum):
    TITLE = "title"
    DIRECTOR = "director"
    CAST_MEMBER = "cast members"


def search_movie(file_path):
    with open(file_path, "r") as json_file:
        try:
            json_data = json.load(json_file)
        except json.JSONDecodeError:
            json_data = {}
            with open(file_path, "w") as write_file:
                json.dump(json_data, write_file)
    if json_data == {} or len(json_data["movies"]) == 0:
        print("There are no movies in your collection. Returning to the main menu.\n")
        return
    print("\n┌────────────────────────────────────┐")
    print("│      - = - Movie Search - = -      │")
    print("│ What would you like to search for? │")
    print("╞════════════════════════════════════╡")
    print("│ 1. Title                           │")
    print("│ 2. Director                        │")
    print("│ 3. Cast member                     │")
    print("│ 4. Return to the main menu         │")
    print("└────────────────────────────────────┘")
    try:
        search_type_input = int(input("\nMake your selection (1-4): ").strip())
    except ValueError:
        print("Invalid input. Please choose a number.")
        return search_movie(file_path)
    match search_type_input:
        case 1:
            search_type = SearchType.TITLE
        case 2:
            search_type = SearchType.DIRECTOR
        case 3:
            search_type = SearchType.CAST_MEMBER
        case 4:
            print("Returning to the main menu.\n")
            return
        case _:
            print("Invalid choice. Please choose a number between 1 and 4.\n")
            return search_movie(file_path)
    search_term = input("Please enter your search term: ").strip()
    search_results = search_movies(json_data, search_type, search_term)
    search_results = sorted(search_results, key = lambda x: (x.release_year, x.title))
    if len(search_results) == 0:
        print("No movies were found. Restarting search.\n")
        return search_movie(file_path)
    lines = []
    lines.append("- = - Movie Search - = -")
    lines.append(f"{len(search_results)} movies found.")
    for result in search_results:
        lines.append(f"x. {result.title} ({result.release_year})")
    max_length = len(max(lines, key=len))
    print("\n┌" + "─" * (max_length + 2) + "┐")
    print("│ " + "- = - Movie Search - = -".center(max_length) + " │")
    print("| " + f"{len(search_results)} movies found.".center(max_length) + " │")
    print("╞" + "═" * (max_length + 2) + "╡")
    i = 1
    for movie in search_results:
        print("│ " + f"{i}. {movie.title} ({movie.release_year})".ljust(max_length) + " │")
        i += 1
    print("└" + "─" * (max_length + 2) + "┘")
    try:
        movie_choice_input = int(input(f"\nWhich movie do you want to view? 1 - {len(search_results)} to choose or {len(search_results) + 1} to restart the search. ").strip())
    except ValueError:
        print("Incorrect input. Please choose a number the next time. Restarting search.\n")
        return search_movie(file_path)
    if movie_choice_input > len(search_results) + 1 or movie_choice_input <= 0:
        print("Invalid choice. Restarting search.\n")
        return search_movie(file_path)
    elif movie_choice_input == len(search_results) + 1:
        print("Restarting search.\n")
        return search_movie(file_path)
    chosen_movie = search_results[movie_choice_input - 1]
    chosen_movie.print()
    new_search_input = input("\nWould you like to start a new search (Y/N)? ").strip()
    if new_search_input.lower() == "y" or new_search_input.lower() == "yes":
        print("Starting new search.\n")
        return search_movie(file_path)
    elif new_search_input.lower() == "n" or new_search_input.lower() == "no":
        print("Returning to main menu.\n")
    else:
        print("Invalid input. Returning to main menu.\n")


def search_movies(json, search_type, search_term):
    movies = json_to_movies(json)
    results = []
    for movie in movies:
        match search_type:
            case SearchType.TITLE:
                if search_term.lower() in movie.title.lower():
                    results.append(movie)
            case SearchType.DIRECTOR:
                if search_term.lower() in movie.director.lower():
                    results.append(movie)
            case SearchType.CAST_MEMBER:
                for member in movie.cast:
                    if search_term.lower() in member.lower():
                        results.append(movie)
    return results


def json_to_movies(json):
    movies = []
    for movie in json["movies"]:
        new_movie = Movie(
            movie["title"],
            movie["release_year"],
            movie["director"],
            movie["cast"],
            movie["summary"],
            movie["id"],
        )
        movies.append(new_movie)
    return movies
