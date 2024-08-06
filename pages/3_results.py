import streamlit as st

st.title("Results")

st.markdown("""
            The plot below shows a histogram of low temperatures for games in the 2023-24 NBA season. We are 
            probably unconcerned with most of the values. The relevant ones are the extreme values on the left -- the 5th percentile 
            is 22 degrees Fahrenheit, so the vast majority of games are scheduled such that the temperatures are not that extreme.


            """)

st.image("assets/low_plot.png", caption="Some of these game days were cold.")


st.markdown("""
The plot below is a histgram of precipitation values, _conditional on having some precipitation_. Most game days have zero precipitation (nearly 7% of the games last year were played in Los Angeles or Las Vegas), and with few exceptions, the values for the entire day were less than a couple inches.
""")

st.image("assets/pos_precip.png", caption="Looks like a power law?")


st.markdown("""
We can immediately identify games that had potentially higher risk of postponement (again, after the fact) by looking at games with extreme values of either low temperature or high precipitation. We already
know that none of these games were actually postponed, but we can quickly use the data to identify some specific games:
- Minnesota at Boston, 1/10/24. Low temp: 42.64°, precipitation: 90.28mm, max wind speed: 33.38 mph
- Orlando at OKC, 1/13/24. Low temp: 4.33°, precipitation: 0.0mm, max wind speed: 27.63 mph
- Cleveland at Atlanta, 3/6/24. Low temp: 54.64°, precipitation: 67.03mm, max wind speed: 14.97 mph
- OKC at Minnesota, 1/20/24. Low temp: -5.57°, precipitation: 0.0mm, max wind speed: 9.22 mph
""")


st.markdown("""
Finally, to put together our measure of extreme weather, we make our final huge assumption that cold weather by itself is typically not a reason for postponement, so we can combine 
low temperature and precipitation by taking the geometric mean of the two _percentile_ measures. This measure has no interpretation by itself, but the highest values (i.e., games in the coldest and snowiest environments) would
presumably have higher possibility of postponement.
""")

st.image("assets/combined.png", caption="The shape is due to the large number of games with zero precipitation.")

st.write("")
st.write("")
st.markdown("""
### Disclaimer
            
Again, this is a toy example, so one really should not take away any conclusions from this data.

These "analyses" can be immediately improved by
- Using forecasts instead of actual weather data
- Taking averages across previous years to assess variability in weather
- Using a more sophisticated metric to combine low temperature and precipitation
- Identify higher-leverage games that would be more costly (across various dimensions) to postpone
- Using actual postponed games to quantify actual likelihoods of postponement
- Constructing counterfactual schedules to see which are robust to extreme weather conditions
- Assessing whether improved schedule construction over time has resulted in fewer postponements
""")