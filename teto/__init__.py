from .client import TetoClient
from .exceptions import TetoException, TetoAPIError, TetoRateLimitError
from .http_engines import HttpEngine
from .models import BaseModel

__title__ = "teto"
__author__ = "tetoguys"
__license__ = "MIT"
__copyright__ = "Copyright 2026-present tetoguys"
__version__ = "1.0.0"

__all__ = [
    "TetoClient",
    "TetoException",
    "TetoAPIError",
    "TetoRateLimitError",
    "HttpEngine",
    "BaseModel",
]
