"""
Expert LLM Application - Main entry point

This application allows users to ask questions to different AI experts
(Medical, Legal, Financial) and receive contextual responses.
"""
import streamlit as st
from dotenv import load_dotenv

import config
import utils
import ui_components as ui


# Load environment variables
load_dotenv()


def setup_page() -> None:
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title=config.APP_TITLE,
        page_icon=config.APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("専門家に質問しよう！")


def check_requirements() -> None:
    """Check if all requirements are met before running the app."""
    if not utils.check_api_key():
        ui.show_error(config.API_KEY_ERROR)
        st.stop()


def handle_user_interaction(selected_expert: str, user_input: str) -> None:
    """
    Handle user interaction when the submit button is clicked.
    
    Args:
        selected_expert: The selected expert type
        user_input: User's question input
    """
    if not utils.validate_user_input(user_input):
        ui.show_warning(config.EMPTY_QUESTION_WARNING)
        return
    
    with ui.show_loading_spinner():
        response = utils.generate_expert_response(user_input, selected_expert)
    
    if response.startswith("エラー"):
        ui.show_error(response)
    else:
        ui.show_response(response)


def main() -> None:
    """
    Main application logic.
    
    Sets up the page, checks requirements, and handles user interactions.
    """
    # Initial setup
    setup_page()
    check_requirements()
    
    # Render UI components
    ui.render_sidebar()
    
    # Create main layout
    col1, col2 = st.columns(config.COLUMN_RATIOS)
    
    with col1:
        selected_expert = ui.render_expert_selector()
    
    with col2:
        user_input = ui.render_question_input()
        
        if ui.render_submit_button():
            handle_user_interaction(selected_expert, user_input)


if __name__ == "__main__":
    main()