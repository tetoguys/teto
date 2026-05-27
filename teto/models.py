from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseModel(ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseModel":
        pass
