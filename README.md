# Cartoonizer

A simple python program to convert an image into a cartoon like pencil sketch in no time.
Simple to use and fast.

## How it works 
It uses a OpenCV built-in pencil sketch function which makes the work easier.
```python
sketch_gray, sketch_color = cv2.pencilSketch(image_, sigma_s=60, sigma_r=0.07, shade_factor=0.04)
```
It uses Streamlit to provide an interface for using the app.

Yoi can find the live app [here](https://share.streamlit.io/josiasaurel/cartoonizer/cartoonizer.py)