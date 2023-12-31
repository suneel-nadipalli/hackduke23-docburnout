import streamlit as st

PAGE_CONFIG = {"page_title":"patteRN Health", 
               "page_icon":"🏥", 
               "layout":"centered", 
               "initial_sidebar_state":"collapsed"}

st.set_page_config(**PAGE_CONFIG)

from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit.components.v1 as components
from google.oauth2 import service_account
from gsheetsdb import connect
from streamlit_autorefresh import st_autorefresh
from st_circular_progress import CircularProgress
import joblib

from streamlit_extras.altex import line_chart, get_stocks_data

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

st.header("My Progress")

st.write("")
st.write("")

@st.cache_data(ttl=1)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

X = np.array(df)

timestamps = list(range(len(df)))

data_points = list(svm_clf.predict(X))

# ========== CREATE PLOT ==========

plot_df = pd.DataFrame({'Time (sec)': timestamps, 'Stress Level': data_points})

stocks = get_stocks_data()
line_chart(
    data=plot_df,
    x="Time (sec)",
    y="Stress Level"
)

st.write("")
st.write("")

dummy1, col1, col2, dummy2 = st.columns([1, 3, 3, 1])
newsize = (150, 150)

with col1:

    prog_level = 5

    if 0 < prog_level <= 20:
          circ_prog_bl = CircularProgress(
          label="Burnout",
          value=prog_level,
          size="Large",
          key="circ_prog_bl",
          color='green')
    elif 20 < prog_level <= 40:
          circ_prog_bl = CircularProgress(
          label="Burnout",
          value=prog_level,
          size="Large",
          key="circ_prog_bl",
          color='yellow')
    elif 40 < prog_level <= 60:
          circ_prog_bl = CircularProgress(
          label="Burnout",
          value=prog_level,
          size="Large",
          key="circ_prog_bl",
          color='orange')
    elif 60 < prog_level <= 80:
          circ_prog_bl = CircularProgress(
          label="Burnout",
          value=prog_level,
          size="Large",
          key="circ_prog_bl",
          color='red')
    elif 80 < prog_level <= 100:
          circ_prog_bl = CircularProgress(
          label="Burnout",
          value=prog_level,
          size="Large",
          key="circ_prog_bl",
          color='red')

    circ_prog_bl.st_circular_progress()

with col2:

    pred_level = svm_clf.predict(np.array(df.tail(1)))[0]

    prog_level = int((pred_level/5)*100)

    if 0 < prog_level <= 20:
          circ_prog_sl = CircularProgress(
          label="Stress",
          value=prog_level,
          size="Large",
          key="circ_prog_sl",
          color='green')
    elif 20 < prog_level <= 40:
          circ_prog_sl = CircularProgress(
          label="Stress",
          value=prog_level,
          size="Large",
          key="circ_prog_sl",
          color='yellow')
    elif 40 < prog_level <= 60:
          circ_prog_sl = CircularProgress(
          label="Stress",
          value=prog_level,
          size="Large",
          key="circ_prog_sl",
          color='orange')
    elif 60 < prog_level <= 80:
          circ_prog_sl = CircularProgress(
          label="Stress",
          value=prog_level,
          size="Large",
          key="circ_prog_sl",
          color='red')
    elif 80 < prog_level <= 100:
          circ_prog_sl = CircularProgress(
          label="Stress",
          value=prog_level,
          size="Large",
          key="circ_prog_sl",
          color='red')
    
    circ_prog_sl.st_circular_progress()

# footer = st.container()
# with footer:
#     col1, col2, col3= st.columns((2,1,1))
#     with col1:
#         st.write("Home")
#     with col2:
#         st.write("Actions")
#     with col3:
#         st.write("Daily Checkin")
