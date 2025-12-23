import streamlit as st
import openai

st.title("AI Code Error Explainer")

code = st.text_area("Paste your code here")
error = st.text_area("Paste the error message here")

if st.button("Explain Error"):
    st.write("Analyzing...")
