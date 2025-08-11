from enum import Enum
from typing import List, Optional, Union

from core.movie import Movie


class SearchType(Enum):
    TITLE = "title"
    DIRECTOR = "director"
    CAST_MEMBER = "cast members"


SEARCH_OPTIONS: dict[int, SearchType] = {
    1: SearchType.TITLE,
    2: SearchType.DIRECTOR,
    3: SearchType.CAST_MEMBER
}
SEARCH_OPTIONS_MENU_LINES = [
    "1. Title",
    "2. Director",
    "3. Cast member",
    "4. Return to the main menu"
]


def print_menu(header: str, subheader: str) -> None:
    lines = [header, subheader] + SEARCH_OPTIONS_MENU_LINES
    max_length = max(len(line) for line in lines)
    print("\n┌" + "─" * (max_length + 2) + "┐")
    for line in lines[:2]:
        print("│ " + line.center(max_length) + " │")
    print("╞" + "═" * (max_length + 2) + "╡")
    for line in lines[2:]:
        print("│ " + line.ljust(max_length) + " │")
    print("└" + "─" * (max_length + 2) + "┘")


def prompt_search_type(header: str, subheader: str) -> Optional[SearchType] | str:
    print_menu(header, subheader)
    try:
        choice = int(input("\nMake your selection (1-4): ").strip())
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


def display_results(results: List[Movie], header: str) -> None:
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


def prompt_movie_choice(results: List[Movie], prompt_text: str) -> Union[Movie, str, None]:
    max_choice = len(results) + 1
    try:
        choice = int(input(f"\n{prompt_text} 1 - {len(results)} to choose or {max_choice} to start over. ").strip())
    except ValueError:
        print("Invalid input. Starting over.")
        return None
    if choice == max_choice:
        print("Starting over.")
        return "restart"
    if 1 <= choice <= len(results):
        return results[choice - 1]
    print("Invalid choice. Starting over.")
    return None
