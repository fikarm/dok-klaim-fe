import httpx
import json
from streamlit.runtime.uploaded_file_manager import UploadedFile


class Client:
    def __init__(
        self,
        session_id: str,
        base_url: str = "http://0.0.0.0:8080",
        agent_name: str | None = None,
    ):
        self.session_id = session_id
        self.base_url = base_url

    def cobi(self):
        return httpx.get(f"{self.base_url}/cobi")

    def invoke(self, agent_name: str, message: str, pdf: UploadedFile | None = None):
        file = [("files", (pdf.name, pdf.read(), pdf.type))] if pdf else None

        payload = {"thread_id": self.session_id, "message": message}

        # print("url", f"{self.base_url}/{agent_name}/invoke")
        # print("file", file)
        # print("payload", payload)

        response = httpx.post(
            f"{self.base_url}/{agent_name}/invoke",
            data=payload,
            files=file,
            timeout=300,
        )

        return response
