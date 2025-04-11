import streamlit as st
from utils import extract_text_from_pdf
from critique_engine import generate_critique



st.set_page_config(page_title="Research Paper Critique Generator")

st.title("Research Paper Critique Generator")

uploaded_file = st.file_uploader("Upload your research paper (PDF)", type=["pdf"])

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf("temp.pdf")

    if text:
        with st.spinner("Generating critique..."):
            critique = generate_critique(text)

        st.subheader("Section Summary")
        st.write(critique["summary"])

        st.subheader("Identified Research Gaps")
        st.write(critique["research_gap"])

        st.subheader("Suggestions for Improvement")
        st.write(critique["suggestions"])
    else:
        st.error("Could not extract text from the PDF.")