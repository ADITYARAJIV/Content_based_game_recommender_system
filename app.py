import pandas as pd
import pickle
import streamlit as st
from game_recommender_engine import recommendation_system

games_dict = pickle.load(open('games_dict.pkl', 'rb'))
game = pd.DataFrame(games_dict)
recommendations = []
st.title("Game Recommender System")

selected_game_name = st.selectbox(
    'How would you like to be contacted ?',
    game['Name'].values)

if st.button('recommend'):
    try:
        recommendations = recommendation_system(selected_game_name, game)
        '''
        for game_name in list(recommendations):
            st.text(game_name)
        '''
        df = pd.DataFrame(recommendations, columns = ['Game_names'])
        st.table(df)
    except Exception as e:
        st.write(e)
        st.write('No recommendations')
