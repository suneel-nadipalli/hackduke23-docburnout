import streamlit as st

st.title("APP NAME HERE")

st.header("My Progress")
st.write("GRAPH HERE")

col1, col2 = st.columns(2)

with col1:
   st.header("Stress Level")
   st.write("MEDIUM STRESS CIRCLE CHART HERE")

with col2:
   st.header("Burnout Level")
   st.write("MEDIUM BURNOUT CIRCLE CHART HERE")

st.button("Daily Checkin")

st.write("")
st.write("")

footer = st.container()
with footer:
    col1, col2, col3= st.columns((2,1,1))
    with col1:
        st.write("Home")
    with col2:
        st.write("Actions")
    with col3:
        st.write("Daily Checkin")
