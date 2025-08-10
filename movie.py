import uuid


class Movie:
    def __init__(self, title, release_year, director=None, cast=[], summary=None, id=uuid.uuid4().hex):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.director = director
        self.cast = cast
        self.summary = summary
    
    def __repr__(self):
        print(f"Movie({self.id},{self.title},{self.director},{self.cast},{self.summary})")
    
    def __str__(self):
        return f"{self.id}\n{self.title}\n{self.director}\n{self.cast}\n{self.summary}"
    
    def print(self):
        lines = []
        lines.append(f"{self.title} ({self.release_year})")
        lines.append(f"Directed by: {self.director}")
        for member in self.cast:
            lines.append(member)
        max_length = len(max(lines, key=len))
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
            print("│ " + line.center(max_length) + " │")
        print ("└" + "─" * (max_length + 2) + "┘")


def movie_to_dictionary(movie):
    return {
        "id": movie.id,
        "title": movie.title,
        "release_year": movie.release_year,
        "director": movie.director,
        "cast": movie.cast,
        "summary": movie.summary,
    }


def wrap_summary(summary, max_length):
    summary_lines = []
    if len(summary) <= max_length:
        return summary_lines
    words = summary.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_length:
            if current_line:
                current_line += " "
            current_line += word
        else:
            summary_lines.append(current_line)
            current_line = word
    if current_line:
        summary_lines.append(current_line)
    return summary_lines
