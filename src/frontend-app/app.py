import streamlit as st

workflow_page = st.Page("pages/workflow.py", title="Summarize ad workflow", icon=":material/dashboard:", default=True)
describe_page = st.Page("pages/describe.py", title="Describe and identify purpose", icon=":material/looks_one:")
saliency_page = st.Page("pages/saliency.py", title="Assess saliency", icon=":material/filter_1:")
cognitive_page = st.Page("pages/cognitive.py", title="Assess cognitive load", icon=":material/looks_two:")
summarize_page = st.Page("pages/summarize.py", title="Summarize outputs from two llm's", icon=":material/looks_3:")

pg = st.navigation([workflow_page, describe_page, saliency_page, cognitive_page, summarize_page])
st.set_page_config(page_title="Neurons", page_icon=":material/edit:")
pg.run()
