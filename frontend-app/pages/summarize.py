import streamlit as st
import requests
from config import ENDPOINT_ROOT

output1 = st.text_input(label="Llm output 1")
output2 = st.text_input(label="Llm output 2")

run_process = st.button("Run process")

if run_process:

    with st.status("Running process"):

        response = requests.post(url=f"{ENDPOINT_ROOT}/process-c/",
                                params={"first_output": output1,
                                        "second_output": output2})

        st.write("process response:")
        st.write(response.json())

if run_process:
    st.button("Reset")