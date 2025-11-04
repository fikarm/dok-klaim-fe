import uuid
import streamlit as st
from frontend.pages.single_rule_page.schema import ChatHistory
from frontend.pages.single_rule_page.client import Client
from streamlit.runtime.uploaded_file_manager import UploadedFile


def init_thread_id():
    if "thread_id" in st.session_state:
        return st.session_state.thread_id

    # thread_id = st.query_params.get("thread_id")
    # if thread_id:
    #     return thread_id

    thread_id = str(uuid.uuid4())
    st.session_state.thread_id = thread_id

    return st.session_state.thread_id


def init_history() -> ChatHistory:
    if "history" in st.session_state:
        return st.session_state.history

    history = ChatHistory()
    st.session_state.history = history

    return st.session_state.history


def init_pdf_uploaded() -> UploadedFile | None:
    if "pdf" in st.session_state:
        return st.session_state.pdf

    st.session_state.pdf = None

    return st.session_state.pdf


def init_client():
    if "client" in st.session_state:
        return st.session_state.client

    if "thread_id" in st.session_state:
        init_thread_id()

    st.session_state.client = Client(st.session_state.thread_id)

    return st.session_state.client
