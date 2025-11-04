import httpx
from src.schema import UserInput


class AgentClient:
    def __init__(
        self,
        base_url: str = "http://0.0.0.0",
        agent: str | None = None,
        timeout: float | None = None,
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.agent = agent

    async def ainvoke(
        self,
        message: str,
        model: str | None = None,
        thread_id: str | None = None,
        user_id: str | None = None,
    ):
        request = UserInput(message=message)

        request.thread_id = thread_id
        if user_id:
            request.user_id = user_id

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/{self.agent}/invoke",
                json=request.model_dump(),
                timeout=self.timeout,
            )
            return response.json()
