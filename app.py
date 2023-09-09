import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="APP NAME HERE"
    # ,page_icon="CHECK"
    )

st.title("APP NAME HERE")

st.header("My Progress")
image_1 = Image.open('img/Orange Circle.png')
st.image(image_1)

col1, col2 = st.columns(2)
newsize = (200, 200)

with col1:
    image_2 = Image.open('img/Orange Circle.png')
    # image_2 = Image.open('C:/Users/Jared Bailey/Desktop/Home/Hackathon/Hack for Good/2023/Orange Circle.png')
    image_2 = image_2.resize(newsize)
    st.image(image_2)
    st.header("Stress Level")

   
with col2:
    image_3 = Image.open('img/Red Circle.png')
    # image_3 = Image.open('C:/Users/Jared Bailey/Desktop/Home/Hackathon/Hack for Good/2023/Red Circle.png')
    image_3 = image_3.resize(newsize)
    st.image(image_3)
    st.header("Burnout Level")

st.button("Daily Checkin")

st.write("")
st.write("")

# footer = st.container()
# with footer:
#     col1, col2, col3= st.columns((2,1,1))
#     with col1:
#         st.write("Home")
#     with col2:
#         st.write("Actions")
#     with col3:
#         st.write("Daily Checkin")
