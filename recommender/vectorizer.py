from sklearn.feature_extraction.text import TfidfVectorizer

def create_vectorizer():
    return TfidfVectorizer(stop_words='english')

def vectorize_data(df, vectorizer):
    return vectorizer.fit_transform(df['combined'])
