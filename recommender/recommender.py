from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_recommendations(title, df, vectors):
    idx = df[df['title'] == title].index[0]
    sim_scores = cosine_similarity(vectors[idx], vectors).flatten()
    sim_indices = sim_scores.argsort()[-6:-1][::-1]
    return df['title'].iloc[sim_indices].tolist()
