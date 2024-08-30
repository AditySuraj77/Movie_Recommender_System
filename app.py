import streamlit as st
import pickle
import pandas as pd
movie_dict = pickle.load(open('moviesList.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity_movies_recommed = pickle.load(open('SimilarityScore.pkl','rb'))

def recommed(movie_name):
    index = movies[movies['title'] == movie_name].index[0]
    distances = similarity_movies_recommed[index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommed_movie = []
    for i in movie_list:
        recommed_movie.append(movies.iloc[i[0]].title)
    return recommed_movie

st.title('Recommender System')

selected_movie_name = st.selectbox('Movie',movies['title'].values)

if st.button('Recommended'):
    recommended = recommed(selected_movie_name)
    for i in recommended:
        st.write(i)



