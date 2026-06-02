import streamlit as st
from ai_engine import analyze_log

st.set_page_config(
    page_title="AI Splunk Copilot",
    layout="wide"
)

st.title("🧠 AI Splunk Copilot")

st.write(
    "Analyze Splunk and system logs using a local LLM powered by Ollama."
)

log_input = st.text_area(
    "Paste a log entry",
    height=250
)

if st.button("Analyze Log"):
    if log_input.strip():

        with st.spinner("Analyzing..."):
            result = analyze_log(log_input)

        st.subheader("Analysis")
        st.markdown(result)

    else:
        st.warning("Please paste a log first.")