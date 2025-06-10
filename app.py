import streamlit as st
from qa_chain import get_answer

st.set_page_config(page_title="Medical Assistant RAG")
st.title("🩺 Clinical Question Answering")
query = st.text_input("Ask a medical question:")

if query:
    with st.spinner("Thinking..."):
        response = get_answer(query)
        st.markdown(f"### Answer\n{response}")