import streamlit as st

st.title("Suggestions")

st.divider()
col_0_1, col_0_2 = st.columns([4,1])

with col_0_1:
    st.header("Sleep")
    st.write("Nap 20 minutes to reduce tiredness")
with col_0_2:
    st.write("")
    Complete1 = st.button('Complete')
st.divider()
