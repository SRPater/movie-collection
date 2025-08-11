from enum import Enum
from typing import List, Optional, Union

from json_manager import load_movies
from movie import Movie


class SearchType(Enum):
    TITLE = "title"
    DIRECTOR = "director"
    CAST_MEMBER = "cast members"


SEARCH_MENU: str = """
┌────────────────────────────────────┐
│      - = - Movie Search - = -      │
│ What would you like to search for? │
╞════════════════════════════════════╡
│ 1. Title                           │
│ 2. Director                        │
│ 3. Cast member                     │
│ 4. Return to the main menu         │
└────────────────────────────────────┘
"""
SEARCH_OPTIONS: dict[int, SearchType] = {
    1: SearchType.TITLE,
    2: SearchType.DIRECTOR,
    3: SearchType.CAST_MEMBER
}


def prompt_search_type() -> Optional[SearchType] | str:
    print(SEARCH_MENU)
    try:
        choice = int(input("Make your selection (1-4): ").strip())
    except ValueError:
        print("Invalid input. Please choose a number.\n")
        return "invalid"
    if choice == 4:
        return None
    if choice not in SEARCH_OPTIONS:
        print("Invalid choice. Please choose a number between 1 and 4.\n")
        return "invalid"
    return SEARCH_OPTIONS.get(choice)


def search_movies(
        movies: List[Movie],
        search_type: SearchType,
        search_term: str
) -> List[Movie]:
    term = search_term.casefold()
    results = []
    for movie in movies:
        title = movie.title.casefold()
        director = (movie.director or "").casefold()
        cast = [member.casefold() for member in movie.cast]
        match search_type:
            case SearchType.TITLE if term in title:
                results.append(movie)
            case SearchType.DIRECTOR if term in director:
                results.append(movie)
            case SearchType.CAST_MEMBER if any(term in member for member in cast):
                results.append(movie)
            case _:
                pass
    return results


def display_results(results: List[Movie]) -> None:
    header = "- = - Movie Search - = -"
    count_line = f"{len(results)} movies found."
    max_length = max(
        len(header),
        len(count_line),
        *(len(f"{i}. {movie.title} ({movie.release_year})") for i, movie in enumerate(results, start=1)),
    )
    print("\n┌" + "─" * (max_length + 2) + "┐")
    print("│ " + header.center(max_length) + " │")
    print("│ " + count_line.center(max_length) + " │")
    print("╞" + "═" * (max_length + 2) + "╡")
    for i, movie in enumerate(results, start=1):
        line = f"{i}. {movie.title} ({movie.release_year})"
        print("│ " + line.ljust(max_length) + " │")
    print("└" + "─" * (max_length + 2) + "┘")


def prompt_movie_choice(results: List[Movie]) -> Union[Movie, str, None]:
    max_choice = len(results) + 1
    try:
        choice = int(input(f"\nWhich movie do you want to view? 1 - {len(results)} to choose or {max_choice} to restart the search. ").strip())
    except ValueError:
        print("Invalid input. Restarting search.")
        return None
    if choice == max_choice:
        print("Restarting search.")
        return "restart"
    if 1 <= choice <= len(results):
        return results[choice - 1]
    print("Invalid choice. Restarting search.")
    return None


def search_movie(file_path: str) -> None:
    movies = load_movies(file_path)
    if not movies:
        print("There are no movies in your collection. Returning to the main menu.\n")
        return
    while True:
        search_type = prompt_search_type()
        if search_type is None:
            print("Returning to the main menu.\n")
            return
        if search_type == "invalid":
            continue
        if not isinstance(search_type, SearchType):
            continue
        search_term = input("Please enter your search term: ").strip()
        results = sorted(
            search_movies(movies, search_type, search_term),
            key=lambda m: (m.release_year, m.title),
        )
        if not results:
            print("No movies were found. Restarting the search.\n")
            continue
        display_results(results)
        choice = prompt_movie_choice(results)
        if choice == "restart" or choice is None:
            continue
        if isinstance(choice, Movie):
            choice.print()
        new_search = input("\nWould you like to start a new search (Y/N)? ").strip().lower()
        if new_search in ("y", "yes"):
            print("Starting a new search.\n")
            continue
        print("Returning to the main menu.\n")
        break
