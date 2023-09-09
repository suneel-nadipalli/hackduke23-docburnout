import streamlit as st

st.title("Maslach Burnout Inventory Test")

form = st.form(key='my_form')

question_01 = form.slider("I feel run down and drained of physical or emotional energy", 1, 7, 4)

form.write("")
form.write("")
question_02 = form.slider("I have negative thoughts about my job", 1, 7, 4)

form.write("")
form.write("")
question_03 = form.slider("I am harder and less sympathetic with people than perhaps they deserve", 1, 7, 4)

form.write("")
form.write("")
question_04 = form.slider("I am easily irritated by small problems, or by my co-workers and team", 1, 7, 4)

form.write("")
form.write("")
question_05 = form.slider("I feel misunderstood or unappreciated by my co-workers", 1, 7, 4)

form.write("")
form.write("")
question_06 = form.slider("I feel that I have no one to talk to", 1, 7, 4)

form.write("")
form.write("")
question_07 = form.slider("I feel that I am achieving less than I should", 1, 7, 4)

form.write("")
form.write("")
question_08 = form.slider("I feel under an unpleasant level of pressure to succeed", 1, 7, 4)

form.write("")
form.write("")
question_09 = form.slider("I feel that I am not getting what I want out of my job", 1, 7, 4)

form.write("")
form.write("")
question_10 = form.slider("I feel that I am in the wrong organization or the wrong profession", 1, 7, 4)

form.write("")
form.write("")
question_11 = form.slider("I am frustrated with parts of my job", 1, 7, 4)

form.write("")
form.write("")
question_12 = form.slider("I feel that organizational politics or bureaucracy frustrate my ability to do a good job", 1, 7, 4)

form.write("")
form.write("")
question_13 = form.slider("I feel that there is more work to do than I practically have the ability to do", 1, 7, 4)

form.write("")
form.write("")
question_14 = form.slider("I feel that I do not have time to do many of the things that are important to doing a good quality job", 1, 7, 4)

form.write("")
form.write("")
question_15 = form.slider("I find that I do not have time to plan as much as I would like to", 1, 7, 4)

submit = form.form_submit_button('Submit')
