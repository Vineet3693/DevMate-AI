import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from config.settings import load_config

st.set_page_config(
    page_title="DevMate AI",
    page_icon="🤖",
    layout="wide"
)

def main():
    st.title("🤖 DevMate AI")
    st.markdown("AI-powered development assistant")
    
    st.sidebar.title("Navigation")
    st.sidebar.markdown("Use the pages above to access different tools")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("🔍 Code Analysis")
        st.write("Analyze your code for quality and issues")
        
    with col2:
        st.header("🛠️ Code Generator")
        st.write("Generate code from natural language")

if __name__ == "__main__":
    main()
