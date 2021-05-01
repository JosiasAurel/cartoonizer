import streamlit as st
import cv2

st.title("Cartoonizer")
st.write("Convert your images into cartoon photos")

image = st.file_uploader("Import Image", type=["png", "jpeg"])
if image is not None:
    sketch_gray, sketch_color = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    st.image(sketch_gray)
    st.image(sketch_color)

st.write("By Josias Aurel")