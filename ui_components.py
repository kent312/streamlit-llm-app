"""
UI components for the Expert LLM Application
"""
import streamlit as st
from typing import Optional

import config


def render_sidebar() -> None:
    """Render the application sidebar with information."""
    with st.sidebar:
        st.info(config.SIDEBAR_INFO)
        
        # Additional sidebar content can be added here
        st.markdown("---")
        st.markdown("### 使い方")
        st.markdown(
            "1. 左側から専門家を選択\n"
            "2. 質問を入力\n"
            "3. 「質問する」ボタンをクリック"
        )


def render_expert_selector() -> str:
    """
    Render the expert selection radio buttons.
    
    Returns:
        str: Selected expert type
    """
    return st.radio(
        "専門家を選択",
        options=list(config.EXPERT_PROFILES.keys()),
        index=0,
        help="質問に最も適した専門家を選択してください"
    )


def render_question_input() -> str:
    """
    Render the question input text area.
    
    Returns:
        str: User's question input
    """
    return st.text_area(
        "質問を入力してください",
        placeholder="ここに質問を入力...",
        height=config.TEXT_AREA_HEIGHT,
        help="専門家に聞きたいことを詳しく記入してください"
    )


def render_submit_button() -> bool:
    """
    Render the submit button.
    
    Returns:
        bool: True if button is clicked
    """
    return st.button("質問する", type="primary", use_container_width=True)


def show_response(response: str) -> None:
    """
    Display the generated response.
    
    Args:
        response: The response text to display
    """
    st.success(config.RESPONSE_HEADER)
    st.markdown(response)


def show_error(message: str) -> None:
    """
    Display an error message.
    
    Args:
        message: Error message to display
    """
    st.error(message)


def show_warning(message: str) -> None:
    """
    Display a warning message.
    
    Args:
        message: Warning message to display
    """
    st.warning(message)


def show_loading_spinner() -> st.spinner:
    """
    Return a loading spinner context manager.
    
    Returns:
        st.spinner: Spinner context manager
    """
    return st.spinner(config.GENERATING_RESPONSE)