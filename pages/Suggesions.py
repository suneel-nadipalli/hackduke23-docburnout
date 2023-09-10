import streamlit as st

st.title("Suggestions")

col_0_1, col_0_2 = st.columns(2)

with col_0_1:
    st.header("Sleep")
    st.write("Nap 20 minutes to reduce tiredness")
with col_0_2:
    Complete1 = st.form_submit_button('Complete')
