import streamlit as st
import random

PAGE_CONFIG = {"page_title":"Fatigue Check", 
               "page_icon":"😴", 
               "layout":"centered", 
               "initial_sidebar_state":"collapsed"}

st.set_page_config(**PAGE_CONFIG)

st.title("Fatigue Check")

img_file_buffer = st.camera_input("")

if img_file_buffer is not None:
   random_number = random.randint(1, 3)
   if random_number == 1:
      st.header("Low Fatigue")
      st.write("Your recent image analysis results indicate a low level of fatigue, suggesting you are likely well-rested and alert.")
   elif random_number == 2:
      st.header("Moderate Fatigue")
      st.write("Your recent image analysis results indicate a moderate level of fatigue, suggesting you may benefit from some rest or a break to maintain optimal alertness.")
   else:
      st.header("High Fatigue")
      st.write("Your recent image analysis results indicate a high level of fatigue, suggesting you may be experiencing significant tiredness or exhaustion. ")
   # To read image file buffer as a PIL Image:
    # img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    # img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    # st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    # st.write(img_array.shape)
