import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header


st.set_page_config( page_icon=":open_mailbox_with_raised_flag:",layout="wide")
st.sidebar.success("📁Select a page above") 


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
  

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_code = load_lottieurl("https://lottie.host/8845d9f4-5e6f-4260-a40b-cc17bbfa88e6/55LjGCWcDI.json")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")    

with st.sidebar:


    st.title(":violet[✨ About this website]")
    st.subheader("##")
    st.write("👨‍💻 This project is created by Alok Kuamr, student of XI-C of Mayur Public School in Delhi.")
    st.write("🔰 Thi website helps you to edit any image in a very efficent way!!")
    st.write("🔰 Click on the Image Editor Page above to go to the tool")
    st.write("🔰 Click on the Contact Page to contact me and let me know the feedback regarding this too!!l")
    colored_header(label="##", description="##", color_name="violet-70",)
       

st.title("Feel free to share your :violet[Feedback]:upside_down_face:")
colored_header(label="##", description="##", color_name="violet-70",)
left_column, right_column = st.columns((2,1))
with left_column:
  st.write("---")
  st.header("Get In Touch With Me :violet[using the portal down below!!!]")
  st.write("##")
  contact_form = """
    <form action="https://formsubmit.co/alokdelhiind@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
  </form> """

      
  left_column, right_column = st.columns((2,1))
  with left_column:
      st.markdown(contact_form, unsafe_allow_html=True)
  with right_column:
      st_lottie(lottie_code, height=200, key="code")





    
