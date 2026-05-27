import uuid
from typing import Optional, Type

from .http_engines import HttpEngine, SyncEngine, AsyncEngine
from .models import BaseModel


def _handle_response(model_cls: Type[BaseModel], raw_data: dict) -> BaseModel:
    return model_cls.from_dict(raw_data)


class TetoClient:
    BASE_URL = "https://ch.tetr.io/api"

    engine: HttpEngine

    def __init__(self, session_id: Optional[str] = None, async_mode: bool = False):
        self.session_id = session_id or str(uuid.uuid4())
        self.async_mode = async_mode

        if self.async_mode:
            self.engine = AsyncEngine(self.session_id)
        else:
            self.engine = SyncEngine(self.session_id)

    def get_request(self, url: str):
        api_url = f"{self.BASE_URL}/{url}"
        res = self.engine.request(api_url)
        return res

    def close(self):
        return self.engine.close()
