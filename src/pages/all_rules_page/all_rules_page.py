import streamlit as st
from src.pages.all_rules_page.client import Client
from src.pages.all_rules_page import schema
from src.pages.all_rules_page import session
from src.pages.all_rules_page import render
from langchain_core.messages import HumanMessage, AIMessage


def all_rules_page():
    session.init_thread_id()

    session.init_history()

    session.init_client()

    session.init_pdf_uploaded()

    petunjuk = (
        "#### Uji Coba Semua Rule\n"
        # "- Masukkan 1 file pdf dokumen klaim\n"
        # "- Tanyakan satu rule ke dalam chat\n"
        # "- Percakapan ini tidak disimpan dan akan hilang ketika muat ulang\n"
        "---"
    )
    st.markdown(petunjuk)

    render.render_history()

    # read user prompt
    prompt = st.chat_input(
        "Cek kelengkapan berkas klaim BPJS ...",
        accept_file="multiple",
        file_type=[
            "pdf",
            # "md"  # sementara md dulu, karena convert pdf ke md mengalami out of memory di server 10.1.1.240
        ],
    )

    if prompt:
        # simpan file upload di session
        if prompt.files is not None:
            st.session_state.pdf = prompt.files

        history: schema.ChatHistory = st.session_state.history

        # render bulb
        human_message = HumanMessage(prompt.text)
        # render.render_human_message(HumanMessage(st.session_state.user_id))
        render.render_human_message(HumanMessage(prompt.text))
        history.messages.append(human_message)

        # client call
        client: Client = st.session_state.client
        response = client.invoke("agent_all_rules", prompt.text, st.session_state.pdf)
        print(response.text)
        print("----")
        print(response.json())

        # render response
        ai_message = AIMessage(response.json())
        render.render_ai_message(ai_message)
        history.messages.append(ai_message)
