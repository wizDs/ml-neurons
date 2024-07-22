import streamlit as st
import requests
from config import ENDPOINT_ROOT

image_path = st.text_input(label="Image path")
heatmap_path = st.text_input(label="Heatmap path")

if image_path and heatmap_path:
    cols = st.columns(2)
    with cols[0]:
        st.image(image=image_path)
    with cols[1]:
        st.image(image=heatmap_path)

run_workflow = st.button("Run workflow")

if run_workflow:

    with st.status("Running workflow"):

        response = requests.post(url=f"{ENDPOINT_ROOT}/workflow/",
                                params={"image_path": image_path,
                                        "heatmap_path": heatmap_path,
                                        "all": True})

        st.write("workflow response:")
        st.write(response.json())

if run_workflow:
    st.button("Reset")