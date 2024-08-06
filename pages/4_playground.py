import streamlit as st

st.title("Playground")

st.write("You can play with the data here -- choose a specific game and you can see the weather data for that game and a score representing how extreme (compared to the rest of the games in the season) that day's weather was. To make it a little easier, particularly extreme weather games are marked with an asterisk (*).")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

games = pd.read_csv("assets/game_data_2023_2024.csv")
games['addStar'] = ""
games.loc[games['percentile_score'] > 95, 'addStar'] = "*"
games['gameSlug'] = games['awayTeam'] + " at " + games['homeTeam'] + ", " + games['homeDateTime'] + games['addStar']

# Special
games.loc[(games['homeTeam'] == "ORL") & (games['homeDateTime'] < "2023-12-20"), 'venue_name'] = "Amway Center"

st.write("")

game = st.selectbox("Select a game from the 2023-24 season", games['gameSlug'], index=None)

if game is None:
    st.write("")
    st.write("")
    empty_plot = sns.histplot(games['score']).set_title("Geometric Mean of Low Temperature and Precipitation")
 
    # Display the plot in Streamlit
    st.pyplot(empty_plot.figure)
else:
    st.markdown(f"## {game}")

    chosen_game = games.loc[games['gameSlug'] == game, ['venue_name', 'low_temperature', 'precipitation (mm)', 'percentile_score', 'score']]
    st.dataframe(chosen_game[['venue_name', 'low_temperature', 'precipitation (mm)', 'percentile_score',]], hide_index=True)

    chosen_plot = sns.histplot(games['score']).set_title("Geometric Mean of Low Temperature and Precipitation")

    plt.axvline(chosen_game['score'].iloc[0], 0, 150, color='k')

    st.pyplot(chosen_plot.figure)

    if chosen_game['percentile_score'].iloc[0] < 95:
        st.write("This game is almost surely going to happen.")
    elif chosen_game['percentile_score'].iloc[0] < 99:
        st.write("This game is probably going to happen.")
    else:
        st.write("The weather is terrible but the game will still most likely happen.")



