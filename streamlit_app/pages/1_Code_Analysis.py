
import streamlit as st

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from agents.code_analyzer import CodeAnalyzer
from models.analysis_models import AnalysisRequest
from components.code_editor import CodeEditor
from components.results_display import ResultsDisplay
from components.sidebar import render_sidebar

st.set_page_config(page_title="Code Analysis", page_icon="🔍")

def main():
    st.title("🔍 Code Analysis")
    
    settings = render_sidebar()
    
    code, language = CodeEditor.render("analysis_editor")
    
    if st.button("Analyze Code", type="primary"):
        if code.strip():
            with st.spinner("Analyzing..."):
                analyzer = CodeAnalyzer()
                request = AnalysisRequest(code=code, language=language)
                result = analyzer.analyze_code(request)
                ResultsDisplay.show_analysis_result(result)
        else:
            st.warning("Please enter code to analyze")

if __name__ == "__main__":
    main()
