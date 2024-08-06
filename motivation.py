import streamlit as st

st.title("NBA Game Postponement")

st.markdown("""
Since many of the inputs to schedule construction are likely proprietary, I wanted to construct
a toy example of how one could use publicly available data to construct a metric regarding a specific
aspect of a schedule.
            
After some very cursory research, I found that weather-related postponements have been somewhat rare in the NBA. The reasons are pretty obvious -- NBA games are played indoors, so the main disruption to games is primarily due to travel or fan safety. Home teams
who play in cities with very cold weather are also likely to have airports designed to handle this kind of weather. The last example I could find was Washington at Detroit,
scheduled for February 1, 2023, though that game was _not_ postponed due to bad weather in Detroit, but due to Pistons unable
to make it back home because of inclement weather in Dallas. Ironically, a Pistons at Mavericks game in 2016 was also postponed due to 
extreme cold in Dallas. This illustrates how the risk of postponement is likely due to things like extreme variation in weather patterns rather than simply having an extreme
measurement like a large amount of precipitation or a very low temperature value.[^1]
            
Though postponements are rare, I still decided to gather weather data for the most recent NBA season to see whether one could
identify specific games that might be at risk of postponement due to inclement weather. While I will not be comparing different counterfactual schedules to see
if any are robust to weather, I will be constructing a very simple metric that we might use to identify games that have a higher likelihood of
being postponed due to weather.
            
I should make clear that this example makes huge assumptions and also takes advantage of full knowledge (i.e., the schedule is already known in advance, and 
I also use actual weather data and not forecasts).
            
[^1]: In fact, there is a Sixers home game (against the Kings) that was postponed due to condensation forming on an unseasonably _warm_ day.   
""")


st.write("")
st.write("")
st.image("https://library.sportingnews.com/styles/crop_style_16_9_desktop/s3/2021-08/2006-storm-outside-madison-square-garden_1qtxufuoyhacu1i75wh6q115yu.jpg?itok=DqIFNo2g", caption="Source: Sporting News")            
