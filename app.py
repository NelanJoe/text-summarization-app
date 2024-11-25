import streamlit as st
import os
from utils import summary_text, extract_text_from_pdf


def main():
    st.set_page_config(
        page_title="Summarizer App",
        page_icon="📚",
        layout="wide"
    )

    choice = st.sidebar.selectbox("Select your choice", ["Summarize Text", "Summarize Document"])    

    # Summarize Text
    if choice ==  "Summarize Text":
        st.subheader("Summarize Text")
        input_text = st.text_area("Enter your text here", height=200)

        if input_text is not None:
            if st.button("Summarize Text"):
                col1, col2 = st.columns([1,1])
                with col1: 
                    st.markdown("**Extracted text from your text:**")
                    st.write(input_text)
                with col2:
                    result = summary_text(input_text)
                    st.markdown("**Summary:**")
                    st.success(result)

    # Summarize Document PDF  
    else:
        st.subheader("Summarize Document")
        input_file = st.file_uploader("Upload your document", type="pdf")

        if input_file is not None:
            if st.button("Convert PDF to Text"):
                # Extracting text from PDF
                with open("temp.pdf", "wb") as f:
                    f.write(input_file.read())

                text_result = extract_text_from_pdf("temp.pdf")
                
                # define 2 columns
                col1, col2 = st.columns([1,1])
                # Column for results from extracted text
                with col1:
                    st.markdown("**Extracted text from PDF file:**")
                    st.write(text_result)

                # Column for results from txtai
                with col1:
                    st.markdown("**Summary:**")
                    summary_result = summary_text(text_result)
                    st.success(summary_result)
                    os.remove("temp.pdf") # Delete temporary file

        
if __name__ == "__main__":
    main()