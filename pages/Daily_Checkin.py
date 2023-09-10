import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed", layout="centered")

st.title("Maslach Burnout Inventory Test")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
  st.write("1) Never")
with col2:
  st.write("2) A few times a year or less")
with col3:
  st.write("3) Once a month or less")
with col4:
  st.write("4) A few times a month")
with col5:
  st.write("5) Once a week")
with col6:
  st.write("6) A few times a week")
with col7:
  st.write("7) Every day")

form = st.form(key='my_form')

question_01 = form.slider("1) I feel run down and drained of physical or emotional energy", 1, 7, 4)

form.write("")
form.write("")
question_02 = form.slider("2) I have negative thoughts about my job", 1, 7, 4)

form.write("")
form.write("")
question_03 = form.slider("3) I am harder and less sympathetic with people than perhaps they deserve", 1, 7, 4)

form.write("")
form.write("")
question_04 = form.slider("4) I am easily irritated by small problems, or by my co-workers and team", 1, 7, 4)

form.write("")
form.write("")
question_05 = form.slider("5) I feel misunderstood or unappreciated by my co-workers", 1, 7, 4)

form.write("")
form.write("")
question_06 = form.slider("6) I feel that I have no one to talk to", 1, 7, 4)

form.write("")
form.write("")
question_07 = form.slider("7) I feel that I am achieving less than I should", 1, 7, 4)

form.write("")
form.write("")
question_08 = form.slider("8) I feel under an unpleasant level of pressure to succeed", 1, 7, 4)

form.write("")
form.write("")
question_09 = form.slider("9) I feel that I am not getting what I want out of my job", 1, 7, 4)

form.write("")
form.write("")
question_10 = form.slider("10) I feel that I am in the wrong organization or the wrong profession", 1, 7, 4)

form.write("")
form.write("")
question_11 = form.slider("11) I am frustrated with parts of my job", 1, 7, 4)

form.write("")
form.write("")
question_12 = form.slider("12) I feel that organizational politics or bureaucracy frustrate my ability to do a good job", 1, 7, 4)

form.write("")
form.write("")
question_13 = form.slider("13) I feel that there is more work to do than I practically have the ability to do", 1, 7, 4)

form.write("")
form.write("")
question_14 = form.slider("14) I feel that I do not have time to do many of the things that are important to doing a good quality job", 1, 7, 4)

form.write("")
form.write("")
question_15 = form.slider("15) I find that I do not have time to plan as much as I would like to", 1, 7, 4)

submit_button = form.form_submit_button('Submit')

if submit_button:
    score = (question_01 + question_02 + question_03 + question_04 + question_05 + 
            question_06 + question_07 + question_08 + question_09 + question_10 + 
            question_11 + question_12 + question_13 + question_14 + question_15)
    st.header("Your Score: ", score)
    if score < 25:
        st.write("Scores of 0-24 indicated very low burnout.")
    elif score < 50:
        st.write("Scores of 25-49 indicated low burnout.")
    elif score < 75:
        st.write("Scores of 50-74 indicated moderate burnout.")
    else:
        st.write("Scores of 75 and above indicate high burnout.")





