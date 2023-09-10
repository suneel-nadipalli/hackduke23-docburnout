import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed", layout="centered")

# st.title("Fatigue Check")

img_file_buffer = st.camera_input("")

   if img_file_buffer is not None:

      st.write("Your recent image analysis results indicate a low level of fatigue, suggesting you are likely well-rested and alert.")
      st.write("Your recent image analysis results indicate a moderate level of fatigue, suggesting you may benefit from some rest or a break to maintain optimal alertness.")
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
