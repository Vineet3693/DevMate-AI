
from .results_display import ResultsDisplay
import streamlit as st

class CodeEditor:
    @staticmethod
    def render(key="code_editor"):
        code = st.text_area(
            "Enter your code:",
            height=300,
            key=key
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            language = st.selectbox(
                "Language",
                ["python", "javascript", "java", "cpp", "go"],
                key=f"{key}_lang"
            )
        
        return code, language
