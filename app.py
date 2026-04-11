import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# --- Page Setup ---
st.set_page_config(page_title="Movie Matcher Pro", layout="wide")

# --- Load Data & Build Similarity ---
@st.cache_resource
def prepare_engine():
    df = pd.read_csv('processed_movies.csv')
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['tags'].fillna(''))
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return df, cosine_sim

try:
    df, cosine_sim = prepare_engine()
except FileNotFoundError:
    st.error("Please run 'python preprocess.py' first!")
    st.stop()

# --- UI ---
st.title("🎬 AI Movie Recommendation System")
st.write("TMDB Movies Dataset 2024 @kaggle")

selected_movie = st.selectbox("Select a movie:", df['title'].values)

if st.button('Recommend'):
    idx = df[df['title'] == selected_movie].index[0]
    distances = sorted(list(enumerate(cosine_sim[idx])), reverse=True, key=lambda x: x[1])
    
    # Top 5 recommendations
    recs = df.iloc[[i[0] for i in distances[1:6]]]
    
    cols = st.columns(5)
    for i, col in enumerate(cols):
        movie = recs.iloc[i]
        
        # Build image URL (TMDB's public image server)
        # We use w500 for high quality
        poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
        
        with col:
            st.image(poster_url)
            st.subheader(movie['title'])
            
            # Rating and Genre
            st.write(f"⭐ **Rating:** {movie['vote_average']}")
            st.caption(f"**Genres:** {movie['genre']}")
            
            with st.expander("Read Overview"):
                st.write(movie['overview'])

# --- Footer ---
st.markdown("---")
st.caption("Running purely on local hardware and public image assets.")