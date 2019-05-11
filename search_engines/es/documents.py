import mypy_extensions as mx
from datetime import datetime
from typing import List, Dict, Union


class TedDocument(mx.TypedDict):
    comment: str
    description: str
    duration: float
    published_date: datetime
    ratings: List[Dict[str, Union[str, float]]]
    created_at: datetime
