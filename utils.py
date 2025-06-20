"""
Utility functions for the Expert LLM Application
"""
import os
from typing import Optional, List
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

import config


def check_api_key() -> bool:
    """
    Check if OpenAI API key is available in environment variables.
    
    Returns:
        bool: True if API key exists, False otherwise
    """
    return bool(os.getenv("OPENAI_API_KEY"))


def initialize_llm(model_name: str = config.DEFAULT_MODEL, 
                   temperature: float = config.DEFAULT_TEMPERATURE) -> ChatOpenAI:
    """
    Initialize the LLM with specified parameters.
    
    Args:
        model_name: Name of the OpenAI model to use
        temperature: Temperature setting for response generation
        
    Returns:
        ChatOpenAI: Initialized LLM instance
    """
    return ChatOpenAI(model_name=model_name, temperature=temperature)


def create_chat_messages(system_prompt: str, user_question: str) -> List[SystemMessage | HumanMessage]:
    """
    Create chat messages for the LLM.
    
    Args:
        system_prompt: System prompt defining the expert role
        user_question: User's question
        
    Returns:
        list: List of messages for the LLM
    """
    return [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_question)
    ]


def generate_expert_response(user_question: str, expert_type: str) -> str:
    """
    Generate a response from the selected expert.
    
    Args:
        user_question: The user's question
        expert_type: Type of expert selected
        
    Returns:
        str: Generated response or error message
    """
    try:
        llm = initialize_llm()
        system_prompt = config.EXPERT_PROFILES[expert_type]
        messages = create_chat_messages(system_prompt, user_question)
        
        response = llm(messages)
        return response.content
    except KeyError:
        return f"エラー: 無効な専門家タイプ '{expert_type}' が選択されました。"
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"


def validate_user_input(user_input: str) -> bool:
    """
    Validate user input.
    
    Args:
        user_input: Input from the user
        
    Returns:
        bool: True if input is valid, False otherwise
    """
    return bool(user_input and user_input.strip())