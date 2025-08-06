

import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from agents.code_analyzer import CodeAnalyzer
from agents.refactoring_agent import RefactoringAgent
from models.analysis_models import AnalysisRequest
from models.code_models import CodeRequest
from components.code_editor import CodeEditor
from components.results_display import ResultsDisplay
from components.sidebar import render_sidebar

st.set_page_config(page_title="Quality Metrics", page_icon="📊")

def main():
    st.title("📊 Code Quality Metrics")
    
    settings = render_sidebar()
    
    code, language = CodeEditor.render("quality_editor")
    
    col1, col2 = st.columns(2)
    
    with col1:
        analyze_btn = st.button("Analyze Quality", type="primary")
    with col2:
        refactor_btn = st.button("Suggest Refactoring", type="secondary")
    
    if analyze_btn and code.strip():
        with st.spinner("Analyzing code quality..."):
            analyzer = CodeAnalyzer()
            request = AnalysisRequest(code=code, language=language)
            result = analyzer.analyze_code(request)
            
            st.subheader("Quality Metrics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Complexity", f"{result.complexity_score:.2f}")
            with col2:
                st.metric("Issues", len(result.issues))
            with col3:
                st.metric("Suggestions", len(result.suggestions))
            
            ResultsDisplay.show_analysis_result(result)
    
    if refactor_btn and code.strip():
        with st.spinner("Generating refactoring suggestions..."):
            refactor_agent = RefactoringAgent()
            request = CodeRequest(code=code, language=language)
            result = refactor_agent.refactor_code(request)
            ResultsDisplay.show_code_result(result, "Refactored Code")

if __name__ == "__main__":
    main()
