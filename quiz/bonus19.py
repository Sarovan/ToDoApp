import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload image")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if uploaded_image:
    up_img = Image.open(uploaded_image).convert("L")
    st.image(up_img)

if camera_image:
    img = Image.open(camera_image)
    grey_image = img.convert("L")
    st.image(grey_image)
