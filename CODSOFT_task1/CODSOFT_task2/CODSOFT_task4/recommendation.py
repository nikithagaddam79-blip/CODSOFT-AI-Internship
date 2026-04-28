# Movie Recommendation System with Menu (Content-Based)

movies = {
    "Inception": ["sci-fi", "thriller"],
    "Titanic": ["romance", "drama"],
    "Avengers": ["action", "sci-fi"],
    "The Notebook": ["romance", "drama"],
    "Interstellar": ["sci-fi", "drama"],
    "John Wick": ["action", "thriller"],
    "Frozen": ["animation", "family"],
    "Toy Story": ["animation", "comedy"]
}

def recommend(movie_name):
    movie_name = movie_name.strip().title()

    if movie_name not in movies:
        print("\n❌ Movie not found in database.")
        return []

    genres = movies[movie_name]
    recommendations = []

    for movie, g in movies.items():
        if movie != movie_name:
            score = len(set(genres) & set(g))
            if score > 0:
                recommendations.append((movie, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return [movie for movie, score in recommendations]

def main():
    print("🎬 Movie Recommendation System")

    while True:
        print("\nMenu:")
        print("1. Show all movies")
        print("2. Get recommendations")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("\nAvailable Movies:")
            for movie in movies:
                print("-", movie)

        elif choice == "2":
            user_input = input("\nEnter a movie you like: ")
            results = recommend(user_input)

            if results:
                print("\n✅ Recommended Movies:")
                for movie in results:
                    print("-", movie)
            else:
                print("No similar movies found.")

        elif choice == "3":
            print("\n👋 Exiting... Thank you!")
            break

        else:
            print("\n⚠️ Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()