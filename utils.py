import streamlit as st
from txtai.pipeline import Summary
import PyPDF2


@st.cache_resource
def summary_text(text):
    summary = Summary()
    result = summary(text)
    return result

def extract_text_from_pdf(pdf_path):
   with open(pdf_path, "rb") as file:
       reader = PyPDF2.PdfReader(file)
       text = ""
       for page_num in range(len(reader.pages)):
           page = reader.pages[page_num]
           text += page.extract_text()
   return text


