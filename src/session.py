import os
import gc
import uuid
import streamlit as st
from langchain_core.messages.utils import AnyMessage
from frontend import config
from dotenv import load_dotenv
from langchain_ollama import ChatOllama


def init_user_id():
    """
    Get the user ID from session state or URL parameters,
    or create a new one if it doesn't exist.
    """

    # Check if user_id exists in session state
    if "user_id" in st.session_state:
        return st.session_state.user_id

    # Try to get from URL parameters using the new st.query_params
    # if "user_id" in st.query_params:
    #     user_id = st.query_params["user_id"]
    #     st.session_state.user_id = user_id
    #     return user_id

    # Generate a new user_id if not found
    user_id = str(uuid.uuid4())

    # Store in session state for this session
    st.session_state.user_id = user_id

    # Also add to URL parameters so it can be bookmarked/shared
    # st.query_params[user_id] = user_id

    return user_id


def init_threads():
    if "threads" in st.session_state:
        return st.session_state.threads

    threads = []
    st.session_state.threads = threads

    return threads


def init_thread_id():
    if "thread_id" in st.session_state:
        return st.session_state.thread_id

    # thread_id = st.query_params.get("thread_id")
    # if thread_id:
    #     return thread_id

    thread_id = str(uuid.uuid4())
    st.session_state.thread_id = thread_id

    return thread_id


def init_messages():
    if "messages" in st.session_state:
        return st.session_state

    messages = []
    st.session_state.messages = messages
    return messages


# def init_agent_client():
#     if "agent_client" in st.session_state:
#         return st.session_state.agent_client

#     st.session_state.agent_client = Client


def init():
    # generate session id
    if "session_id" not in st.session_state:
        st.session_state.session_id = uuid.uuid4()

    # init message state
    if "messages" not in st.session_state:
        reset_chat()

    reset_query()
    prepare_tmp_dir()


def reset_chat():
    st.session_state.messages = []
    st.session_state.context = None
    gc.collect()


def reset_query():
    st.session_state.query = None
    st.session_state.query_attachment = None


def add_chat(message: AnyMessage):
    st.session_state.messages.append(message)


def prepare_tmp_dir():
    # Create the directory and any necessary parent directories
    # If exist_ok is True, no error is raised if the directory already exists.
    os.makedirs(get_tmp_dir(), exist_ok=True)


def get_tmp_dir():
    # TODO: buat cwd dinamis
    cwd = "/home/itki/projects/rag-dok-klaim/app"
    return os.path.join(cwd, "output", str(st.session_state.session_id))
