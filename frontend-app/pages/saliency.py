import streamlit as st
import requests
from image_utils import show_image_and_decode_to_str
from config import ENDPOINT_ROOT

uploaded_file = st.file_uploader(label="Load Heatmap", type=['png', 'jpg', 'jpeg'])

image: str = show_image_and_decode_to_str(uploaded_file)

run_process = st.button("Run process")

if run_process:

    with st.status("Running process"):

        response = requests.post(url=f"{ENDPOINT_ROOT}/process-a2/",
                                json={"image": image})

        st.write("process response:")
        st.write(response.json())

if run_process:
    st.button("Reset")