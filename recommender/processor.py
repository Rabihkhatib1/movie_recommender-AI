import pandas as pd

def clean_data(df):
    df = df[['title', 'overview', 'genres']].dropna()
    df['combined'] = df['title'] + ' ' + df['overview'] + ' ' + df['genres']
    return df
