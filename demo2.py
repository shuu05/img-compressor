from resizeimage import resizeimage
import PIL
from PIL import Image
import streamlit as st
from io import BytesIO
import glob
import pandas as pd
import os
import sys
import cv2


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


def opn_cv(file):
    img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    new = cv2.imwrite('compress_img.png', img,  [
                      cv2.IMWRITE_PNG_COMPRESSION, 9])
    return new


st.markdown(STYLE, unsafe_allow_html=True)
file = st.file_uploader("Upload file", type="png")

show_file = st.empty()
if not file:
    show_file.info("Please upload a file of type: " + "".join("png"))


if isinstance(file, BytesIO):
    st.write("Original image")
    show_file.image(file)
    st.write("size : ", file.size)
    opn_cv(file)
    st.write("After Compression")
    image = Image.open('compress_img.png')
    st.image(image, caption='compressed image', width=None)
    st.write("size : ", image.size)
    file.close()
