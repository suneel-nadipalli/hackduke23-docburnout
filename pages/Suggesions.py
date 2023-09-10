import streamlit as st

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

st.divider()
col_1_1, col_1_2 = st.columns([4,1])

with col_1_1:
    st.header("Eat")
    st.write("Protein bar to consume 300 calories")
with col_1_2:
    st.write("")
    Complete1 = st.button('Complete')
st.divider()

st.divider()
col_2_1, col_2_2 = st.columns([4,1])

with col_2_1:
    st.header("Meditate")
    st.write("5 minutes to reduce stress levels")
with col_2_2:
    st.write("")
    Complete2 = st.button('Complete')
st.divider()
