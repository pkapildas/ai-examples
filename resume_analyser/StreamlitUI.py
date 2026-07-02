import os
import streamlit as st
import pdfplumber
from groq import Groq
from dotenv import load_dotenv


class PDFExtractor:
    """Handles text extraction operations from document files."""

    @staticmethod
    def extract_text(uploaded_file) -> str:
        """Parses an uploaded PDF file and returns combined plaintext string."""
        text_content = []
        try:
            with pdfplumber.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text_content.append(page_text)
            return "\n".join(text_content)
        except Exception as e:
            st.error(f"Failed to read PDF file: {e}")
            return ""


class GroqClient:
    """Manages secure communication interfaces with the Groq API service."""

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model_name = "llama-3.3-70b-versatile"
        self._validate_credentials()
        self.client = Groq(api_key=self.api_key)

    def _validate_credentials(self):
        """Internal safeguard ensuring API authorization tokens exist."""
        if not self.api_key:
            st.error("Authentication Error: GROQ_API_KEY environment variable is missing.")
            st.stop()

    def get_analysis_stream(self, resume_text: str, job_description: str):
        """Constructs prompts and requests a live completion stream from Groq."""
        system_prompt = (
            "You are an expert technical recruiter and ATS optimization engine. "
            "Analyse the provided resume text against the job description. Output your analysis "
            "using highly structured markdown with these distinct headers: "
            "### 📊 Match Percentage, ### ❌ Missing Keywords, ### ✅ Key Strengths, "
            "### ⚠️ Area of Improvements, and ### 🎯 Actionable Recommendations."
        )

        user_prompt = f"JOB DESCRIPTION:\n{job_description}\n\nRESUME TEXT:\n{resume_text}"

        try:
            return self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,
                max_tokens=2048,
                stream=True
            )
        except Exception as e:
            st.error(f"Groq API connection failure: {e}")
            return None


class StreamlitUI:
    """Orchestrates layout configuration, widgets, and view rendering logic."""

    def __init__(self):
        self.llm_service = GroqClient()
        self.pdf_service = PDFExtractor()

    def render_page_headers(self):
        """Initializes application views and layout footprints."""
        st.set_page_config(page_title="OOP Resume Analyser", layout="wide")
        st.title("📄 Object-Oriented AI Resume Analyser")
        st.subheader("High-fidelity modular resume evaluator powered by Groq & pdfplumber")

    def render_form_inputs(self):
        """Builds dual-column inputs and captures interactive data payloads."""
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 1. Upload Resume")
            uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])
        with col2:
            st.markdown("### 2. Job Description")
            job_description = st.text_area("Paste target expectations here", height=200)
        return uploaded_file, job_description

    def process_analysis(self, uploaded_file, job_description: str):
        """Handles state sequencing validations and triggers generation layers."""
        if not uploaded_file:
            st.warning("Action required: Please upload a resume document.")
            return
        if not job_description.strip():
            st.warning("Action required: Please provide target job descriptions.")
            return

        with st.spinner("Parsing documents and calculating contexts..."):
            resume_text = self.pdf_service.extract_text(uploaded_file)

        if not resume_text.strip():
            st.error("Data Payload Error: Extracted text is empty. Confirm file structure.")
            return

        st.markdown("---")
        st.markdown("### 📊 Comprehensive Diagnostic Report")

        stream_response = self.llm_service.get_analysis_stream(resume_text, job_description)
        if stream_response:
            st.write_stream(stream_response)

    def run(self):
        """Primary execution harness lifecycle hook."""
        self.render_page_headers()
        file_input, description_input = self.render_form_inputs()

        if st.button("🚀 Execute Analytical Profile", use_container_width=True):
            self.process_analysis(file_input, description_input)


if __name__ == "__main__":
    # Bootstraps application context safely using object lifecycle instantiations
    app = StreamlitUI()
    app.run()
