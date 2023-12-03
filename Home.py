import streamlit as st
import json
import requests
from streamlit_extras.colored_header import colored_header
from streamlit_lottie import st_lottie


st.set_page_config(page_title="CS-Project", page_icon=":wave:",layout="wide")



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

def load_lottiefile(filepath: str):
       with open(filepath,"r") as f:
              return json.load(f)
       
lottie_cod = load_lottiefile("C:/Users/PRITAM/Desktop/Chatbot CS-Project/lottiefiles/code.json")
       


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


lottie_cod2 = load_lottieurl("https://lottie.host/1d62ca0e-3826-4e83-bc5c-6cc202429759/vBWnNbgLOK.json")

with st.sidebar:


    st.title(":violet[✨ About this website]")
    st.subheader("##")
    st.write("👨‍💻 This project is created by Alok Kumar, student of XI-C of Mayur Public School in Delhi.")
    st.write("🔰 This website helps you to edit any image in a very efficent way!!")
    st.write("🔰 Click on the Image Editor Page above to go to the tool")
    st.write("🔰 Click on the Contact Page to contact me and let me know the feedback regarding this too!!l")
    colored_header(label="##", description="##", color_name="violet-70",)
       


st.title(":violet[Computer Science - Project📝]")

colored_header(label="Hi, I am Alok:wave:", description="##", color_name="violet-70",)

with st. container():
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header(":violet[Transform Your Photos with Image Editing Web App ]! ")
        st.write(" 💠I am Alok Kumar from class XI-C, and this webapp was created by me for CS Project ")
        st.write("💠Using this webapp,Unleash your creativity with :violet[Image Editing Web App] – image editing solution. Effortlessly enhance your photos, apply stunning filters, achieve professional results without the hassle.")
        st.write("[Check-My First project>](https://my-first-project-appxagafqrlisbpucpbaj7z.streamlit.app/)")

    with right_column:
        st_lottie(lottie_cod, quality="high", height=200, key=None,)


with st. container():
    st.write("---")
    right_column, left_column = st.columns((1,2))
    
    with right_column:
        st_lottie(lottie_cod2, height=200, key="coding")
    
    with left_column:
        st.header(":violet[Key Features:face_with_raised_eyebrow:]")
        st.write("🚩:violet[Advanced Editing Tools:] From basic adjustments to advanced filters, our toolkit empowers you to bring your vision to life. ")
        st.write("🚩:violet[Instant Enhancements:] One-click enhancements for quick and stunning results")
        st.write(":violet[Try it for FREE NOW!!!] ")


colored_header(label="####", description="##", color_name="violet-70",)

    






