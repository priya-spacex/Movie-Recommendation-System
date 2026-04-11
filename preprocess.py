# import pandas as pd

# def clean_data():
#     print("Loading large dataset... please wait.")
#     # low_memory=False prevents crashes with mixed data types
#     df = pd.read_csv('dataset.csv', low_memory=False)
    
#     # Standardize column names
#     df.columns = df.columns.str.strip().str.lower()
#     if 'genres' in df.columns:
#         df.rename(columns={'genres': 'genre'}, inplace=True)

#     print(f"Total movies in file: {len(df)}")

#     # --- THE CRITICAL STEP: HARD FILTERING ---
#     # We only keep movies with a high vote count to save your RAM.
#     # Change 500 to 200 if you want more movies, but stay safe!
#     df = df[df['vote_count'] > 500].copy() 
    
#     print(f"Filtered down to {len(df)} popular movies.")

#     # Select columns and drop empty rows
#     df = df[['id', 'title', 'genre', 'overview']].dropna()

#     # Create tags
#     df['tags'] = df['title'] + " " + df['genre'] + " " + df['overview']
#     df['tags'] = df['tags'].str.lower()

#     # Save the small version
#     df[['id', 'title', 'tags']].to_csv('processed_movies.csv', index=False)
#     print("Success! 'processed_movies.csv' is ready.")

# if __name__ == "__main__":
#     clean_data()

import pandas as pd

def clean_data():
    print("Loading large dataset...")
    df = pd.read_csv('dataset.csv', low_memory=False)
    
    # Clean column names
    df.columns = df.columns.str.strip().str.lower()
    if 'genres' in df.columns: df.rename(columns={'genres': 'genre'}, inplace=True)

    # Filter to save your RAM (Keep movies with 500+ votes)
    df = df[df['vote_count'] > 500].copy() 
    print(f"Filtered down to {len(df)} movies.")

    # Select columns we need for the UI
    # Note: 'vote_average' is the rating, 'poster_path' is the image link
    cols_to_keep = ['id', 'title', 'genre', 'overview', 'vote_average', 'poster_path', 'release_date']
    df = df[cols_to_keep].dropna(subset=['title', 'overview'])

    # Create tags for the engine
    df['tags'] = df['title'] + " " + df['genre'] + " " + df['overview']
    df['tags'] = df['tags'].fillna('').str.lower()

    # Save to CSV
    df.to_csv('processed_movies.csv', index=False)
    print("Success! processed_movies.csv is ready.")

if __name__ == "__main__":
    clean_data()