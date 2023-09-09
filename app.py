import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import streamlit.components.v1 as components

# st.set_page_config(initial_sidebar_state="collapsed")

st.set_page_config(
    page_title="Spa MD"
    # ,page_icon="CHECK"
    )

st.title("Spa MD")

st.header("My Progress")
# image_1 = Image.open('img/Graph.png')
# st.image(image_1)

# Example time series data (timestamps and data points)
timestamps = list(range(30))
data_points = [3, 3, 1, 3, 0, 1, 0, 0, 0, 1, 2, 1, 0, 4, 3, 1, 1, 3, 3, 2, 2, 2, 2, 3, 3, 1, 2, 1, 3, 2]

# Convert timestamps to datetime objects (if they're not already)
timestamps = pd.to_datetime(timestamps)

# Create a time series plot
fig = (plt.figure(figsize=(10, 6)))  # Adjust the figure size as needed
plt.plot(timestamps, data_points, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Stress Level')
plt.title('Stress Data Over 30 Seconds')

# Rotate x-axis labels for better readability (optional)
plt.xticks(rotation=45)

# Adjust the x-axis limits to show 10 minutes of data
# plt.xlim([1, 10])

# Display the plot
plt.grid(True)  # Optionally add grid lines
plt.tight_layout()  # Adjust layout to prevent labels from getting cut off

# fig_html = mpld3.fig_to_html(fig)
# components.html(fig_html, height=600)
st.pyplot(plt)

st.write("")
st.write("")
st.write("")
st.write("")

col1, col2 = st.columns(2)
newsize = (200, 200)

with col1:
    image_2 = Image.open('img/Orange Circle.png')
    # image_2 = Image.open('C:/Users/Jared Bailey/Desktop/Home/Hackathon/Hack for Good/2023/Orange Circle.png')
    image_2 = image_2.resize(newsize)
    st.image(image_2)
    st.header("Stress Level")

   
with col2:
    image_3 = Image.open('img/Red Circle.png')
    # image_3 = Image.open('C:/Users/Jared Bailey/Desktop/Home/Hackathon/Hack for Good/2023/Red Circle.png')
    image_3 = image_3.resize(newsize)
    st.image(image_3)
    st.header("Burnout Level")

daily_checking_button = st.button("Daily Checkin", type="primary")
if daily_checking_button:
    switch_page("Daily_Checkin")



# footer = st.container()
# with footer:
#     col1, col2, col3= st.columns((2,1,1))
#     with col1:
#         st.write("Home")
#     with col2:
#         st.write("Actions")
#     with col3:
#         st.write("Daily Checkin")
