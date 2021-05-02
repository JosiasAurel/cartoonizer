import streamlit as st
import cv2
from PIL import Image
import numpy as np 

st.title("Cartoonizer")
st.write("Convert your images into cartoon photos")

image = st.file_uploader("Import Image", type=["png", "jpeg", "jpg"])
if image is not None:
    # print(image.read())
    image_ = np.array(Image.open(image))
    sketch_gray, sketch_color = cv2.pencilSketch(image_, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    st.image(sketch_gray)
    st.image(sketch_color)
    st.balloons()

st.write("By Josias Aurel")
