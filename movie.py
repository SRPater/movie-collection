import textwrap
import uuid
from typing import List, Optional


class Movie:
    def __init__(
            self,
            title: str,
            release_year: int,
            director: Optional[str] = None,
            cast: Optional[List[str]] = None,
            summary: Optional[str] = None,
            id: Optional[str] = None,
    ):
        self.id: str = id or uuid.uuid4().hex
        self.title: str = title
        self.release_year: int = release_year
        self.director: Optional[str] = director
        self.cast: List[str] = cast or []
        self.summary: Optional[str] = summary
    
    def __repr__(self) -> str:
        return f"Movie({self.id},{self.title},{self.director},{self.cast},{self.summary})"
    
    def __str__(self) -> str:
        return f"{self.id}\n{self.title}\n{self.director}\n{self.cast}\n{self.summary}"
    
    def print(self) -> None:
        lines = [
            f"{self.title} ({self.release_year})",
            f"Directed by: {self.director}",
            *self.cast
        ]
        max_length = len(max(lines, key=len)) if lines else 0
        wrapped_summary = wrap_summary(self.summary, max_length)
        print("\n┌" + "─" * (max_length + 2) + "┐")
        print("│ " + f"{self.title} ({self.release_year})".center(max_length) + " │")
        print("│ " + f"Directed by: {self.director}".center(max_length) + " │")
        print("╞" + "═" * (max_length + 2) + "╡")
        print("│ " + "- - Cast - -".center(max_length) + " │")
        for cast_member in self.cast:
            print("│ " + cast_member.center(max_length) + " │")
        print("╞" + "═" * (max_length + 2) + "╡")
        print("│ " + "- - Summary - -".center(max_length) + " │")
        for line in wrapped_summary:
            print("│ " + line.ljust(max_length) + " │")
        print("└" + "─" * (max_length + 2) + "┘")


def movie_to_dictionary(movie: Movie) -> dict:
    return {
        "id": movie.id,
        "title": movie.title,
        "release_year": movie.release_year,
        "director": movie.director,
        "cast": movie.cast,
        "summary": movie.summary,
    }


def wrap_summary(summary: Optional[str], max_length: int) -> List[str]:
    if not summary:
        return []
    return textwrap.wrap(summary, width=max_length)
