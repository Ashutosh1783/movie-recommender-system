import streamlit as st
import pickle
import pandas as pd


# load data
movies = pickle.load(open('movies (1).pkl', 'rb'))
similarity = pickle.load(open('similarity (4).pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id=i[0]
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# UI
st.title('Movie Recommender System')

option = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)