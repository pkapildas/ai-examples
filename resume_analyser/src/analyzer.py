import os
from groq import Groq
from dotenv import load_dotenv
import streamlit as st


class GroqClient:
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

    def analyze_resume(prompt):
        response = client.chat.completions.create(
            model="llma3-70b-8192",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.3,
            max_token=1024
        )
        return response.choices[0].messages[0].content


load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),

)

