import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed", layout="centered")

st.title("Suggestions")

st.divider()
col_0_1, col_0_2 = st.columns([4,1])

with col_0_1:
    st.header("Sleep")
    st.write("Nap 20 minutes to reduce tiredness")
with col_0_2:
    st.write("")
    Complete0 = st.button('Complete')
st.divider()

col_1_1, col_1_2 = st.columns([4,1])

with col_1_1:
    st.header("Eat")
    st.write("Protein bar to consume 300 calories")
with col_1_2:
    st.write("")
    Complete1 = st.button('Complete ')
st.divider()

col_2_1, col_2_2 = st.columns([4,1])

with col_2_1:
    st.header("Meditate")
    st.write("5 minutes to reduce stress levels")
with col_2_2:
    st.write("")
    Complete2 = st.button('Complete  ')
st.divider()

st.write("")
st.write("")
st.title("Other Options")

st.divider()
col_3_1, col_3_2 = st.columns([4,1])

with col_3_1:
    st.header("Exercise")
    st.write("Promote blood circulations")
with col_3_2:
    st.write("")
    Complete3 = st.button('Complete   ')
st.divider()

col_4_1, col_4_2 = st.columns([4,1])

with col_4_1:
    st.header("Affirmations")
    st.write("Restore your confidence")
with col_4_2:
    st.write("")
    Complete1 = st.button('Complete    ')
st.divider()
