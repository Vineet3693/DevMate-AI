
import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from agents.debug_assistant import DebugAssistant
from models.analysis_models import AnalysisRequest
from components.code_editor import CodeEditor
from components.results_display import ResultsDisplay
from components.sidebar import render_sidebar

st.set_page_config(page_title="Debug Assistant", page_icon="🐛")

def main():
    st.title("🐛 Debug Assistant")
    
    settings = render_sidebar()
    
    code, language = CodeEditor.render("debug_editor")
    
    error_message = st.text_area(
        "Error message (optional):",
        height=100,
        placeholder="Paste any error messages here..."
    )
    
    if st.button("Debug Code", type="primary"):
        if code.strip():
            with st.spinner("Debugging..."):
                debug_assistant = DebugAssistant()
                debug_code = f"{code}\n\nError: {error_message}" if error_message else code
                request = AnalysisRequest(code=debug_code, language=language)
                result = debug_assistant.debug_code(request)
                ResultsDisplay.show_analysis_result(result)
        else:
            st.warning("Please enter code to debug")

if __name__ == "__main__":
    main()
