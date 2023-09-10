import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
from google.oauth2 import service_account
from gsheetsdb import connect
from streamlit_autorefresh import st_autorefresh
from st_circular_progress import CircularProgress
import joblib

# count = st_autorefresh(interval=10000, key="fizzbuzzcounter")

def predict_sl(test_array, model):
    dataframe = pd.DataFrame([test_array], columns=['resp_rate', 'body_temp', 'body_ox', 'heart_rate'])
    pred_level = model.predict(dataframe)

    stress_level_labels = {
    0: "Low/Normal",
    1: "Medium Low",
    2: "Medium",
    3: "Medium High",
    4: "High"
    }

    pred_label = stress_level_labels[pred_level[0]]

    return {"stress_level":pred_level[0], 
            "stress_label": pred_label}

svm_clf = joblib.load('burnout.pkl')

# st.set_page_config(initial_sidebar_state="collapsed")

st.set_page_config(
    page_title="Spa MD"
    # ,page_icon="CHECK"
    )

st.title("Spa MD")

st.header("My Progress")

@st.cache_data(ttl=1)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# for row in df.itertuples():
#     st.write(f"Resp Rate: {row.resp_rate} | Body Temp: {row.body_temp} | Body Ox: {row.body_ox} | Heart Rate: {row.heart_rate}")


X = np.array(df)

# Example time series data (timestamps and data points)
# timestamps = list(range(30))
# data_points = [3, 3, 1, 3, 0, 1, 0, 0, 0, 1, 2, 1, 0, 4, 3, 1, 1, 3, 3, 2, 2, 2, 2, 3, 3, 1, 2, 1, 3, 2]

timestamps = list(range(len(df)))

data_points = list(svm_clf.predict(X))

# Convert timestamps to datetime objects (if they're not already)
timestamps = pd.to_datetime(timestamps)

# Create a time series plot
fig = (plt.figure(figsize=(10, 6)))  # Adjust the figure size as needed
plt.plot(timestamps, data_points, marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Stress Level')
plt.title(f'Stress Data Over {len(df )} Seconds')

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


dummy1, col1, col2, dummy2 = st.columns([1, 3, 3, 1])
newsize = (150, 150)

with col1:
    circ_prog_sl = CircularProgress(
    label="Current Stress Level",
    value=5,
    key="circ_prog_sl")

    circ_prog_sl.st_circular_progress()

   
with col2:

    pred_level = svm_clf.predict(np.array(df.tail(1)))

    st.write(svm_clf.predict(np.array(df.tail(1))))
    
    circ_prog_bl = CircularProgress(
    label="Current Burnout Level",
    value=(pred_level/5)*100,
    key="circ_prog_bl")

    circ_prog_bl.st_circular_progress()

    # image_3 = Image.open('img/Red Circle.png')
    # # image_3 = Image.open('C:/Users/Jared Bailey/Desktop/Home/Hackathon/Hack for Good/2023/Red Circle.png')
    # image_3 = image_3.resize(newsize)
    # st.image(image_3)
    # st.header("Burnout Level")

st.write("")
st.write("")
st.write("")

col_01, col_02, col_03 = st.columns([2.2, 2, 2])
with col_02:
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
