# 🎥 Movie Collection

A handy CLI tool to keep track of a movie collection.
I wrote this as my first personal project for Boot.dev's Backend Developer Path.

## 🛠️ Features

* 🔍 Search for a movie by title, director or cast member
* 🆕 Add a new movie to the collection through prompts from the program
* ✏️ Edit existing movies
* 🗑️ Delete movies from the collection

## ⚙️ Prerequisites

* Python 3.8 or higher
* No external dependencies are required - everything uses Python's standard library

## 📁 Directory structure

```
├─ collection/
│  └─ movies.json           # Movie collection data file
├─ src/
│  ├─ core/
│  │  ├─ input_manager.py   # Movie input logic
│  │  ├─ json_manager.py    # JSON read/write logic
│  │  ├─ movie.py           # Movie class & formatting
│  │  └─ search_manager.py  # Search utilities
│  ├─ features/
│  │  ├─ add_movie.py       # Add movie feature
│  │  ├─ delete_movie.py    # Delete movie feature
│  │  ├─ edit_movie.py      # Edit movie feature
│  │  └─ search_movie.py    # Search feature
│  └─ main.py               # Application entry point
└─ README.md                # Documentation
```

## 🔧 Running the program

1. Make sure the `collection/movies.json` file exists in the **root directory of the project**.
   If not, create it as an empty file.
2. Run the following command from the project root:

```bash
python3 src/main.py
```

## 🎬 Usage

Once you start the program, you'll see a menu where you can:

* Search for movies
* Add new movies
* Edit existing movies
* Delete movies

Just follow the on-screen prompts — the program will guide you through each step.

## 🎞️ Example output

When you view or interact with a movie, it's displayed in a neat little box like this:

```
┌──────────────────────────────────────────────────────────┐
│ The Lord of the Rings: The Fellowship of the Ring (2001) │
│                Directed by: Peter Jackson                │
╞══════════════════════════════════════════════════════════╡
│                       - - Cast - -                       │
│                       Elijah Wood                        │
│                       Ian McKellen                       │
│                      Orlando Bloom                       │
│                        Sean Bean                         │
│                        Sean Astin                        │
│                       Andy Serkis                        │
│                     Viggo Mortensen                      │
│                      Cate Blanchett                      │
│                     Christopher Lee                      │
╞══════════════════════════════════════════════════════════╡
│                     - - Summary - -                      │
│ A meek Hobbit from the Shire and eight companions set    │
│ out on a journey to destroy the powerful One Ring and    │
│ save Middle-earth from the Dark Lord Sauron.             │
└──────────────────────────────────────────────────────────┘
```

## 🤝 Contributing

Found a bug or have an idea for improvement?
Feel free to open an issue or submit a pull request.

## 📜 License

This project is released under the MIT License.

## 📫 Contact

Created by Stefan Pater — feel free to reach out!
