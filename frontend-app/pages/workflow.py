import streamlit as st
import requests
from image_utils import show_image_and_decode_to_str
from config import ENDPOINT_ROOT

input_cols = st.columns(2)

with input_cols[0]:
    image_file = st.file_uploader(label="Load Image", type=['png', 'jpg', 'jpeg'])
with input_cols[1]:
    heatmap_file = st.file_uploader(label="Load Heatmap", type=['png', 'jpg', 'jpeg'])


if (image_file is not None) and (heatmap_file is not None):
    cols = st.columns(2)
    with cols[0]:
        image: str = show_image_and_decode_to_str(image_file)

    with cols[1]:
        heatmap: str = show_image_and_decode_to_str(heatmap_file)

run_workflow = st.button("Run workflow")

if run_workflow:

    with st.status("Running workflow"):

        response = requests.post(url=f"{ENDPOINT_ROOT}/workflow/",
                                json={"image": image,
                                      "heatmap": heatmap,
                                      "all": True})

        st.write("workflow response:")
        st.write(response.json())

if run_workflow:
    st.button("Reset")
