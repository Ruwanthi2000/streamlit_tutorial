import streamlit as st

st.sidebar.title("This is written insid ethe sidebar")
st.sidebar.button("click")
st.sidebar.radio("Pick your gender", ["Male","Female"])

container = st.container()
container.write("This is written inside the contrainer")
st.write("This is written outside the contrainer")