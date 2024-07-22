import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from typing import Optional
from config import ENCODING

def show_image_and_decode_to_str(uploaded_file: UploadedFile) -> Optional[str]:

    if (uploaded_file is not None):
        bytes_data = uploaded_file.read()
        st.image(image=bytes_data)
        decoded_str = bytes_data.decode(ENCODING)
        return decoded_str
