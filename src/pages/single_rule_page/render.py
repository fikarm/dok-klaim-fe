import streamlit as st
from src.core.render import render_human_message, render_ai_message
from src.pages.single_rule_page.schema import ChatHistory
from langchain_core.messages import HumanMessage, AIMessage, AIMessageChunk


def render_history():
    """
    Show message history (preserved across reruns)
    """
    history: ChatHistory = st.session_state.history

    for message in history.messages:

        if isinstance(message, HumanMessage):
            render_human_message(message)

        elif isinstance(message, AIMessage):
            render_ai_message(message)

        elif isinstance(message, AIMessageChunk):
            render_ai_message(message)
