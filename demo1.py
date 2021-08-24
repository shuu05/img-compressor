from resizeimage import resizeimage
import PIL
from PIL import Image
import streamlit as st
from io import BytesIO
import glob
import pandas as pd
import os
import sys


st.write("Img Compressor")


STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""


def img_comp(file):
    # Image.open() can also open other image types
    img = Image.open(file)
    # WIDTH and HEIGHT are integers
    resized_img = img.resize((600, 500))
    resized_img.save("resized_image.png")
    return resized_img


st.markdown(STYLE, unsafe_allow_html=True)
file = st.file_uploader("Upload file", type="png")

show_file = st.empty()
if not file:
    show_file.info("Please upload a file of type: " + "".join("png"))


if isinstance(file, BytesIO):
    st.write("Original image")
    show_file.image(file)
    st.write("size : ", file.size)
    img_comp(file)
    st.write("After Compression")
    image = Image.open('resized_image.png')
    st.image(image, caption='compressed image', width=None)
    st.write("size : ", image.size)
    file.close()
