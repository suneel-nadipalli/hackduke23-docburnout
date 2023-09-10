import streamlit as st

st.title("Suggestions")

form1 = st.form(key='my_form')
form1.header("Sleep")
form1.write("Nap 20 minutes to reduce tiredness")
submit = form1.form_submit_button('Complete')
