# ---- Movie Collection Manager ----

# STEP 1 - Create a list of movies
movies = ["Inception", "Avatar", "Titanic", "Interstellar", "Coco"]
print("Movie collection:", movies)

# STEP 2 - Access the list
print("Total movies:", len(movies))
print("First movie:", movies[0])
print("Last movie:", movies[-1])
print("First three movies:", movies[:3])

# STEP 3 - Modify the list
movies.append("Frozen")
print("\nAfter adding Frozen:", movies)

movies.remove("Coco")
print("After removing Coco:", movies)

movies.sort()
print("Sorted alphabetically:", movies)

movies.reverse()
print("Reversed order:", movies)

# STEP 4 - Create a dictionary for movie details
movie_info = {
    "title": "Inception",
    "genre": "Science Fiction",
    "rating": 9.0
}
print("\nMovie Details:", movie_info)

# STEP 5 - Dictionary operations
print("Genre:", movie_info["genre"])
print("Rating:", movie_info.get("rating", "Not available"))

movie_info["rating"] = 9.5
movie_info["director"] = "Christopher Nolan"
movie_info.pop("rating")

print("Updated Movie Details:", movie_info)

# STEP 6 - Convert two lists into a movie directory
movie_ids = [101, 102, 103, 104, 105]
movie_names = ["Inception", "Avatar", "Titanic", "Interstellar", "Frozen"]

movie_directory = dict(zip(movie_ids, movie_names))

print("\nMovie Directory:", movie_directory)
print("Movie with ID 103:", movie_directory[103])