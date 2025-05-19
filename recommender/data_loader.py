import pandas as pd

def load_movie_data(filepath):
    return pd.read_csv(filepath, low_memory=False)
