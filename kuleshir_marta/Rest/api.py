from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)

class Movie:
    def __init__(self, movie_id, title, director, year, genre):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre

    def to_dict(self):
        return {
            "movie_id": self.movie_id,
            "title": self.title,
            "director": self.director,
            "year": self.year,
            "genre": self.genre
        }

class MovieAPI:
    def __init__(self):
        self.movies = []
        self.load_data()

    def load_data(self):
        try:
            with open("movies.json", "r") as file:
                data = json.load(file)
                self.movies = [Movie(movie["movie_id"], movie["title"], movie["director"], movie["year"], movie["genre"]) for movie in data]
        except FileNotFoundError:
            print("File not found")
            self.movies = []

    def save_data(self):
        data_to_save = [movie.to_dict() for movie in self.movies]
        with open("movies.json", "w") as file:
            json.dump(data_to_save, file)

    def get_movies(self):
        return [movie.to_dict() for movie in self.movies]

    def create_movie(self, data):
        movie_id = random.randint(1, 10000)
        movie = Movie(movie_id, data["title"], data["director"], data["year"], data["genre"])
        self.movies.append(movie)
        self.save_data()
        return movie.to_dict()

    def update_movie(self, movie_id, data):
        movie = self.find_movie_by_id(movie_id)
        if movie is not None:
            if "title" in data:
                movie.title = data["title"]
            if "director" in data:
                movie.director = data["director"]
            if "year" in data:
                movie.year = data["year"]
            if "genre" in data:
                movie.genre = data["genre"]
            self.save_data()
            return movie.to_dict()
        return None

    def delete_movie(self, movie_id):
        movie = self.find_movie_by_id(movie_id)
        if movie is not None:
            self.movies = [m for m in self.movies if m.movie_id != movie_id]
            self.save_data()
            return movie.to_dict()
        return None

    def find_movie_by_id(self, movie_id):
        for movie in self.movies:
            if movie.movie_id == movie_id:
                return movie
        return None

movie_api = MovieAPI()

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movie_api.get_movies())

@app.route('/movies', methods=['POST'])
def create_movie():
    try:
        data = request.get_json()
        if "title" not in data or "director" not in data or "year" not in data or "genre" not in data:
            raise KeyError("Title, director, year, and genre are required fields")
        movie = movie_api.create_movie(data)
        return jsonify(movie)
    except KeyError as e:
        return jsonify({"message": str(e)}), 400

@app.route('/movies/<int:movie_id>', methods=['PATCH'])
def update_movie(movie_id):
    data = request.get_json()
    updated_movie = movie_api.update_movie(movie_id, data)
    if updated_movie is not None:
        return jsonify(updated_movie)
    return jsonify({"message": "Movie not found"}), 404

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    deleted_movie = movie_api.delete_movie(movie_id)
    if deleted_movie is not None:
        return jsonify(deleted_movie), 200
    return jsonify({"message": "Movie not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
