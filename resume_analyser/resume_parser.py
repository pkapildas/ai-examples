import pdfplumber
import streamlit as st


class PDFExtractor:

    def extract_resume_text(pdf_path):
        text =""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    extracted_text = page.extract_text()
                    if extracted_text:
                        text += extracted_text
            return text
        except Exception as e:
            #raise ValueError(f"Failed to read PDF file: {e}")
            st.error(f"Failed to read PDF file: {e}")


