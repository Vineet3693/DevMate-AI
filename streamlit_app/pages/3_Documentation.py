

import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from agents.documentation_agent import DocumentationAgent
from models.code_models import CodeRequest
from components.code_editor import CodeEditor
from components.results_display import ResultsDisplay
from components.sidebar import render_sidebar

st.set_page_config(page_title="Documentation", page_icon="📝")

def main():
    st.title("📝 Documentation Generator")
    
    settings = render_sidebar()
    
    code, language = CodeEditor.render("doc_editor")
    
    doc_type = st.selectbox(
        "Documentation Type",
        ["API Documentation", "Code Comments", "README", "User Guide"]
    )
    
    if st.button("Generate Documentation", type="primary"):
        if code.strip():
            with st.spinner("Generating documentation..."):
                doc_agent = DocumentationAgent()
                request = CodeRequest(code=code, language=language)
                result = doc_agent.generate_docs(request)
                ResultsDisplay.show_code_result(result, "Generated Documentation")
        else:
            st.warning("Please enter code to document")

if __name__ == "__main__":
    main()
