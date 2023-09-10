import streamlit as st

st.title("Suggestions")

col_0_1, col_0_2 = st.coluns(2)

form1 = st.form(key='my_form')
with col_0_1:
    form1.header("Sleep")
    form1.write("Nap 20 minutes to reduce tiredness")
with col_0_2:
    submit = form1.form_submit_button('Complete')
