import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed", layout="centered")

# st.title("Fatigue Check")

img_file_buffer = st.camera_input("")

if img_file_buffer is not None:
   # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)
