import streamlit as st
st.write("Hello ,let's learn how to build a streamlit app together")
st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


st.subheader("Image:- ")
st.image("kid.jpg")

st.subheader("Audio:- ")
st.audio("Audio.mp3")

st.subheader("Video:- ")
st.video("video.mp4")

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

import time
st.balloons()
st.subheader("progress bar")
st.progress(10)

st.subheader("wait the execution")
with st.spinner('Wait for it...'):    
    time.sleep(1)

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

#sidebar
st.sidebar.title("This is written insid ethe sidebar")
st.sidebar.button("click")
st.sidebar.radio("Pick your gender", ["Male","Female"])

container = st.container()
container.write("This is written inside the contrainer")
st.write("This is written outside the contrainer")