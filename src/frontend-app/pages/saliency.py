import streamlit as st
import requests
from config import ENDPOINT_ROOT

heatmap_path = st.text_input(label="Heatmap path")

if heatmap_path:
    st.image(image=heatmap_path)

run_process = st.button("Run process")

if run_process:

    with st.status("Running process"):

        response = requests.post(url=f"{ENDPOINT_ROOT}/process-a2/",
                                params={"image_path": heatmap_path})

        st.write("process response:")
        st.write(response.json())

if run_process:
    st.button("Reset")