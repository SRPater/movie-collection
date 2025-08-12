from typing import List, Optional
from datetime import datetime

from core.movie import Movie

def get_valid_title(existing_movies: List[Movie], current_title: Optional[str] = None) -> str:
    while True:
        prompt = "What is the title of the movie? "
        if current_title:
            prompt = f"What is the new title? (Leave empty to keep '{current_title}') "
        title = input(prompt).strip()
        if current_title and title == "":
            return current_title
        if not title:
            print("Please enter a title.")
        elif len(title) > 100:
            print("A title cannot be longer than 100 characters.")
        elif any(m.title.lower() == title.lower() for m in existing_movies if m.title != current_title):
            print("A movie with that title already exists in the database.")
        else:
            return title


def get_valid_release_year(current_year: Optional[int] = None) -> int:
    while True:
        prompt = "In what year was the movie released? "
        if current_year:
            prompt = f"What is the new release year? (Leave empty to keep {current_year}) "
        year_input = input(prompt).strip()
        if current_year and year_input == "":
            return current_year
        try:
            year = int(year_input)
        except ValueError:
            print("Please enter a year.")
            continue
        if 1900 <= year <= datetime.now().year:
            return year
        print(f"The release year must be between 1900 and {datetime.now().year}.")


def get_director(current_director: Optional[str] = None) -> str:
    prompt = "Who directed the movie? "
    if current_director:
        prompt = f"Who is the new director? (Leave empty to keep '{current_director}') "
    director = input(prompt).strip()
    if current_director and director == "":
        return current_director
    return director


def get_cast(current_cast: Optional[List[str]] = None) -> List[str]:
    prompt = "Who starred in the movie? Separate cast members with commas. "
    if current_cast:
        prompt = "Who is in the new cast? Separate cast members with commas. (Leave empty to keep the current cast) "
    cast_input = input(prompt).strip()
    if current_cast and cast_input == "":
        return current_cast
    return [member.strip() for member in cast_input.split(",") if member.strip()]


def get_summary(current_summary: Optional[str] = None) -> str:
    prompt = "Give a short summary of the movie. "
    if current_summary:
        prompt = f"What is the new summary? (Leave empty to keep the current summary) "
    summary = input(prompt).strip()
    if current_summary and summary == "":
        return current_summary
    return summary
