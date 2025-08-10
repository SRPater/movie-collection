# 🎥 Movie Collection

A handy CLI tool to keep track of a movie collection. I wrote this as my first personal project for Boot.dev's Backend Developer Path.

## 🛠️ Features

* 🔍 Search for a movie by title, director or cast member
* 🆕 Add a new movie to the collection through prompts from the program

## 📁 Directory structure

```
├─ collection/
│  └─ movies.json   - Movie collection file
├─ main.py          - Main application file
├─ movie.py         - Movie class and formatter for showing movies
├─ README.md        - Documentation
└─ search_movie.py  - Search functionality
```

## 🔧 Running the program

First, make sure the `collection/movies.json` file is in the root directory of the program. If not, just add an empty file. Then, run the following command:

`python3 main.py`
