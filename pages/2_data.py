import streamlit as st

st.title("Data")

st.markdown("""
There are three pieces of publicly available data used for this toy example. The NBA has a JSON-formatted schedule available at (https://cdn.nba.com/static/json/staticData/scheduleLeagueV2.json) -- 
previous seasons are also available via the International Broadcaster's Schedule endpoint at stats.nba.com. I can identify the home team for each game and combine that with a geocoded dataset of NBA arenas
to determine the latitude and longitude of each arena. I then use a weather API to gather the appropriate weather for each game (using the geocoordinates along with the date of the game).

For each game, the weather at the home team's arena was gathered for the day of the game. High and low temperatures, along with precipitation and maximum wind speed were recorded. 
Further investigation would involve constructing a more informed metric that combined factors in a useful way, but we can basically assess inclement weather by taking a combination of low temperature and precipitation.

There were six "special" games during the 2023-2024 season. These games were the Paris game between the Cavs and the Nets, the Spurs' games in Austin, and the In Season Tournament semifinals and finals at T-Mobile Arena. None of these
locations or dates involved high risk for inclement weather, but the appropriate weather was still retrieved.
                        
Code for the data gathering and our simple analyses can be found at https://github.com/monstertruck/postponement.
""")
