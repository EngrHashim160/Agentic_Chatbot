import streamlit as st
from src.langgraphAgenticAi.ui.streamlitui.loadUI import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """"
    Loads and runs the Langgraph agenticAI application with streamlit UI.
    This function initilizes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while implementing exception handling for robustness.
    """
    
    # Load UI
    
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    
    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
    
    user_message = st.chat_input("Enter your message: ")
    
    if user_message:
        pass