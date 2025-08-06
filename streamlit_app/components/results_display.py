
import streamlit as st

class ResultsDisplay:
    @staticmethod
    def show_code_result(result, title="Result"):
        st.subheader(title)
        
        if hasattr(result, 'generated_code'):
            st.code(result.generated_code, language=result.language)
        
        if hasattr(result, 'explanation') and result.explanation:
            st.markdown("**Explanation:**")
            st.markdown(result.explanation)
    
    @staticmethod
    def show_analysis_result(result):
        st.subheader("Analysis Results")
        
        if result.issues:
            st.markdown("**Issues Found:**")
            for issue in result.issues:
                st.error(f"**{issue['type']}**: {issue['message']}")
        
        if result.suggestions:
            st.markdown("**Suggestions:**")
            for suggestion in result.suggestions:
                st.info(suggestion)
        
        st.metric("Complexity Score", f"{result.complexity_score:.2f}")
