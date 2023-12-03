import streamlit as st
from PIL import Image, ImageOps, ImageFilter
from rembg import remove
from streamlit_extras.colored_header import colored_header
import requests


page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
Background-image: url("https://images2.alphacoders.com/130/1308898.jpg");
Background-size: cover;
}
[data-testid="stHeader"]{
Background-color: rgba(0,0,0,0);
}
[data-testid="stSidebar"]{
Background-image: url("https://images2.alphacoders.com/130/1308898.jpg");
Background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.success("📁Select a page above")


       

SUPPORTED_FILE_TYPES =['.png','.jpg','.jpeg']

   # Page title
st.title("Image Editor App🖼️")
colored_header(label="Transform Your Photos", description="##", color_name="violet-70",)

   # File uploader
uploaded_file = st.file_uploader("🖼Choose an image...", type=SUPPORTED_FILE_TYPES)

if uploaded_file is not None:
       
       original_image = Image.open(uploaded_file)

       # Display the original image
       st.image(original_image, caption="Original Image", use_column_width=True)

       # Image editing options
       st.sidebar.header("Edit Options")

       # Resize
       new_size = st.sidebar.slider("Resize", 10, 1000, 500)
       resized_image = original_image.resize((new_size, new_size))
       st.image(resized_image, caption="Resized Image", use_column_width=True)

       # Rotate
       rotation_angle = st.sidebar.slider("Rotate", -180, 180, 0)
       rotated_image = original_image.rotate(rotation_angle)
       st.image(rotated_image, caption="Rotated Image", use_column_width=True)

       # Filter
       filter_option = st.sidebar.selectbox("Select Filter", ["None", "Blur", "Contour", "Edge Enhance"])
       if filter_option != "None":
           filters = {"Blur": ImageFilter.BLUR, "Contour": ImageFilter.CONTOUR, "Edge Enhance": ImageFilter.EDGE_ENHANCE}
           filtered_image = original_image.filter(filters[filter_option])
           st.image(filtered_image, caption=f"{filter_option} Filtered Image", use_column_width=True)


       # Download button
st.write("To Downlod edited image right click and`click save image as`.")

with st.sidebar:


    st.title(":violet[✨ About this website]")
    st.subheader("##")
    st.write("👨‍💻 This project is created by Alok Kuamr, student of XI-C of Mayur Public School in Delhi.")
    st.write("🔰 Thi website helps you to edit any image in a very efficent way!!")
    st.write("🔰 Click on the Image Editor Page above to go to the tool")
    st.write("🔰 Click on the Contact Page to contact me and let me know the feedback regarding this too!!l")
    colored_header(label="##", description="##", color_name="violet-70",)

