import streamlit as st
from schema.schema import ChatHistory, Thread
from langchain_core.messages import HumanMessage, AIMessage, AIMessageChunk
from streamlit.elements.widgets.chat import ChatInputValue


def render_history(thread_id: str):
    """
    Show message history (preserved across reruns)
    """
    if not "threads" in st.session_state.threads:
        return

    thread: Thread = st.session_state.threads[thread_id]

    for message in thread.messages:

        if isinstance(message, HumanMessage):
            render_human_message(message)

        elif isinstance(message, AIMessage):
            render_ai_message(message)

        elif isinstance(message, AIMessageChunk):
            render_ai_message(message)


def render_attachment(content: dict):
    # if content["type"] == "image":
    #     with st.container(width=100):
    #         with open(content["filepath"], "rb") as f:
    #             st.image(f.read())
    #         # st.image(base64.b64decode(content["data"]))
    # else:
    # st.download_button(
    #     label=content["filename"],
    #     data=content["filename"],
    #     file_name="data.csv",
    #     mime="text/csv",
    #     icon=":material/download:",
    # )
    st.badge(label=content["filename"])


def render_human_message(message: HumanMessage):
    with st.chat_message("human"):
        content = message.content

        if message.additional_kwargs and "files" in message.additional_kwargs:
            for item in message.additional_kwargs["files"]:
                render_attachment(item)

        if isinstance(content, str):
            st.markdown(content)
        elif isinstance(content, list):
            for item in content:
                if isinstance(item, dict):
                    if item["type"] == "text":
                        st.markdown(item["text"])
                    else:
                        render_attachment(item)
                else:
                    st.markdown(item)


def render_ai_message(message: AIMessage | AIMessageChunk):
    with st.chat_message("ai"):
        st.markdown(message.content)

        return AIMessage(content=message.content)


def render_prompt_message(prompt: ChatInputValue):
    humanMessage = HumanMessage(
        content=prompt.text,
        additional_kwargs={
            "files": [
                {
                    # "filepath": os.path.join(get_tmp_dir(), file.name),
                    "filename": file.name,
                }
                for file in prompt.files
            ]
        },
    )

    render_human_message(humanMessage)
