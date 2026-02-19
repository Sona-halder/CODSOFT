import numpy as np
from collections import defaultdict

# Sample movie ratings data (userId, movieId, rating 1-5)
ratings = [
    (1, 101, 5), (1, 102, 4), (1, 103, 1),  # User 1 ratings
    (2, 101, 5), (2, 104, 3), (2, 105, 5),  # User 2
    (3, 102, 4), (3, 104, 4), (3, 106, 2),  # User 3
    (4, 103, 3), (4, 105, 4), (4, 107, 5),  # User 4
    (5, 101, 4), (5, 106, 3), (5, 107, 4)   # User 5
]

# Movie names (by movieId)
movies = {
    101: "Inception", 102: "The Matrix", 103: "Titanic", 
    104: "Avengers", 105: "RRR", 106: "3 Idiots", 107: "Sholay"
}

def create_rating_matrix(ratings):
    """Convert ratings to user-movie matrix"""
    users = defaultdict(lambda: defaultdict(int))
    for user, movie, rating in ratings:
        users[user][movie] = rating
    return users

def cosine_similarity(user1_ratings, user2_ratings):
    """Calculate similarity between two users"""
    common_movies = set(user1_ratings.keys()) & set(user2_ratings.keys())
    if not common_movies:
        return 0
    
    numerator = sum(user1_ratings[m] * user2_ratings[m] for m in common_movies)
    denom1 = sum(r**2 for r in user1_ratings.values())**0.5
    denom2 = sum(r**2 for r in user2_ratings.values())**0.5
    
    return numerator / (denom1 * denom2) if denom1 * denom2 != 0 else 0

def get_recommendations(user_id, ratings_matrix, k=3):
    """Find top K movie recommendations for user"""
    user_ratings = ratings_matrix[user_id]
    
    # Find similar users
    similarities = {}
    for other_user in ratings_matrix:
        if other_user != user_id:
            sim = cosine_similarity(user_ratings, ratings_matrix[other_user])
            similarities[other_user] = sim
    
    # Sort by similarity
    similar_users = sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:k]
    
    # Predict ratings for unrated movies
    recommendations = defaultdict(float)
    for similar_user, sim_score in similar_users:
        for movie, rating in ratings_matrix[similar_user].items():
            if movie not in user_ratings:
                recommendations[movie] += sim_score * rating
    
    # Return top recommendations
    sorted_recs = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [(movie, score) for movie, score in sorted_recs[:3]]

def main():
    """Interactive movie recommender"""
    ratings_matrix = create_rating_matrix(ratings)
    
    print("🎬 Movie Recommendation System (Like Netflix!)")
    print("Users:", list(ratings_matrix.keys()))
    print("Movies:", [f"{id}: {name}" for id, name in movies.items()])
    print()
    
    while True:
        try:
            user_id = int(input("Enter your user ID (1-5) or 'q' to quit: "))
            if user_id == 'q':
                break
                
            if user_id not in ratings_matrix:
                print("User not found! Try 1-5.")
                continue
            
            print(f"\nYour ratings: {dict(ratings_matrix[user_id])}")
            recs = get_recommendations(user_id, ratings_matrix)
            
            print(f"\n🎥 Recommendations for User {user_id}:")
            for movie_id, score in recs:
                movie_name = movies.get(movie_id, "Unknown")
                print(f"  📺 {movie_name} (predicted rating: {score:.1f})")
            
        except ValueError:
            print("Enter number 1-5 or 'q'")
        except KeyboardInterrupt:
            print("\n👋 Thanks for using Movie Recommender!")
            break

if __name__ == "__main__":
    main()
