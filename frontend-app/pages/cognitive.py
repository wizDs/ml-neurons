import streamlit as st
import requests
from config import ENDPOINT_ROOT

image_path = st.text_input(label="Image path")

if image_path:
    st.image(image=image_path)

run_process = st.button("Run process")

if run_process:

    with st.status("Running process"):

        response = requests.post(url=f"{ENDPOINT_ROOT}/process-b/",
                                params={"image_path": image_path})

        st.write("process response:")
        st.write(response.json())

if run_process:
    st.button("Reset")