from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    DEV_HOST = "localhost:9200"
