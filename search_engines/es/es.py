from dataclasses import dataclass, InitVar
from datetime import datetime
from pathlib import Path

import pandas as pd
from elasticsearch import Elasticsearch
from tqdm import tqdm

import search_engines.es.config as c
from search_engines.es.documents import TedDocument


@dataclass()
class ES:
    host: InitVar[str] = c.Config.DEV_HOST
    data_fp: InitVar[Path] = Path(__file__).resolve().parents[2] / "data" / "ted_main.csv"

    def __post_init__(self, host: str, data_fp: Path):
        self.es = Elasticsearch(host)
        self.df = pd.read_csv(data_fp)

    def insert(self) -> None:
        for index, line in tqdm(self.df.iterrows()):
            doc = TedDocument(comment=line["comments"],
                              description=line["description"],
                              duration=line["duration"],
                              published_at=line["published_date"],
                              rating=line["rating"],
                              created_at=datetime.now())
            self.es.create(index='ted', id=index, body=doc)


if __name__ == '__main__':
    main()
