import time
import asyncio
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import requests
import aiohttp

from .exceptions import TetoAPIError, TetoRateLimitError


class HttpEngine(ABC):
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.headers = {"X-Session-ID": self.session_id}

    @abstractmethod
    def request(self, url: str) -> Dict[str, Any]:
        pass

    def close(self):
        pass


class SyncEngine(HttpEngine):
    def __init__(self, session_id: str):
        super().__init__(session_id)
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self._last_request_time = 0.0

    def _apply_rate_limit(self):
        elapsed = time.time() - self._last_request_time
        if elapsed < 1.0:
            time.sleep(1.0 - elapsed)
        self._last_request_time = time.time()

    def request(self, url: str) -> Dict[str, Any]:
        self._apply_rate_limit()
        response = self.session.get(url)

        if response.status_code == 429:
            raise TetoRateLimitError("Rate limit exceeded (Sync)")

        data = response.json()
        if not data.get("success", False):
            raise TetoAPIError(data.get("error", "API Error"))
        return data.get("data", {})

    def close(self):
        self.session.close()


class AsyncEngine(HttpEngine):
    def __init__(self, session_id: str):
        super().__init__(session_id)
        self._session: Optional[aiohttp.ClientSession] = None
        self._lock = asyncio.Lock()

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(headers=self.headers)
        return self._session

    async def request(self, url: str) -> Dict[str, Any]:
        session = await self._get_session()

        async with self._lock:
            await asyncio.sleep(1.0)
            async with session.get(url) as response:
                if response.status == 429:
                    raise TetoRateLimitError("Rate limit exceeded (Async)")

                data = await response.json()
                if not data.get("success", False):
                    raise TetoAPIError(data.get("error", "API Error"))
                return data.get("data", {})

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()
