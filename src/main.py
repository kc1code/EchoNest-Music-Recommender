import streamlit as st
from recommend import df, recommend_songs

# Set custom Streamlit page config
st.set_page_config(
    page_title="Music Recommender 🎵",
    page_icon="🎧",
    layout="centered"
)

st.title("🪺 EchoNest - Music Recommender")

# Add a description below the title
st.markdown(
    """
    🎶 Welcome to **EchoNest** — your personal guide to discovering music you'll love!
    
    Pick a song you enjoy, and we'll find similar tunes to match your vibe.  
    Dive into the world of melodies, rhythms, and beats curated just for you! 🎧
    """
)

song_list = sorted(df['song'].dropna().unique())
selected_song = st.selectbox("🎵 Select a song:", song_list)

if st.button("🚀 Recommend Similar Songs"):
    with st.spinner("Finding similar songs..."):
        recommendations = recommend_songs(selected_song)
        if recommendations is None:
            st.warning("Sorry, song not found.")
        else:
            st.success("Top similar songs:")
            st.table(recommendations)
