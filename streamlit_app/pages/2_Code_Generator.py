
import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from agents.code_generator import CodeGenerator
from models.code_models import CodeRequest
from components.results_display import ResultsDisplay
from components.sidebar import render_sidebar

st.set_page_config(page_title="Code Generator", page_icon="🛠️")

def main():
    st.title("🛠️ Code Generator")
    
    settings = render_sidebar()
    
    prompt = st.text_area(
        "Describe what code you want to generate:",
        height=150
    )
    
    language = st.selectbox(
        "Target Language",
        ["python", "javascript", "java", "cpp", "go"]
    )
    
    if st.button("Generate Code", type="primary"):
        if prompt.strip():
            with st.spinner("Generating..."):
                generator = CodeGenerator()
                request = CodeRequest(code=prompt, language=language)
                result = generator.generate_code(request)
                ResultsDisplay.show_code_result(result, "Generated Code")
        else:
            st.warning("Please enter a description")

if __name__ == "__main__":
    main()
