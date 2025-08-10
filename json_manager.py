from movie import Movie


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
