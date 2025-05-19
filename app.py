from recommender.recommender import data_loader, preprocessor, vectorizer, recommender

if __name__ == "__main__":
    df = data_loader.load_movie_data('data/movies_metadata.csv')
    df = preprocessor.clean_data(df)
    
    tfidf = vectorizer.create_vectorizer()
    tfidf_matrix = vectorizer.vectorize_data(df, tfidf)

    movie_title = input("Enter a movie title: ")
    if movie_title in df['title'].values:
        recommendations = recommender.get_recommendations(movie_title, df, tfidf_matrix)
        print("\nRecommended movies:")
        for movie in recommendations:
            print(f"- {movie}")
    else:
        print("Movie not found.")
