import json
from typing import List

from core.movie import Movie, movie_to_dictionary


def json_to_movies(json_data: dict) -> List[Movie]:
    movies: List[Movie] = []
    for movie_dict in json_data.get("movies", []):
        try:
            movies.append(
                Movie(
                    title=movie_dict.get("title", ""),
                    release_year=movie_dict.get("release_year", 0),
                    director=movie_dict.get("director", ""),
                    cast=movie_dict.get("cast", []),
                    summary=movie_dict.get("summary", ""),
                    id=movie_dict.get("id"),
                )
            )
        except Exception as e:
            print(f"Skipping invalid movie entry: {e}")
    return movies


def movies_to_json(movies: List[Movie]) -> dict:
    return {"movies": [movie_to_dictionary(movie) for movie in movies]}


def load_movies(file_path: str) -> List[Movie]:
    try:
        with open(file_path, "r") as file:
            json_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    return json_to_movies(json_data)


def save_movies(file_path: str, movies: List[Movie]) -> None:
    try:
        with open(file_path, "w") as file:
            json.dump(movies_to_json(movies), file, indent=4)
    except Exception as e:
        print(f"Error saving movies: {e}")
