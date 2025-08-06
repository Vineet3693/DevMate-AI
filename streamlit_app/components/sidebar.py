
import streamlit as st

def render_sidebar():
    st.sidebar.title("🤖 DevMate AI")
    st.sidebar.markdown("---")
    
    st.sidebar.info("Select a tool from the pages above")
    
    st.sidebar.markdown("### Settings")
    model = st.sidebar.selectbox(
        "Model",
        ["mixtral-8x7b-32768", "llama2-70b-4096", "gemma-7b-it"]
    )
    
    temperature = st.sidebar.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1
    )
    
    return {"model": model, "temperature": temperature}
