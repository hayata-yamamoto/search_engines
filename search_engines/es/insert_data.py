from datetime import datetime

import pandas as pd
from elasticsearch import Elasticsearch
from tqdm import tqdm

from search_engines.core.path_manager import PathManager
from search_engines.es.config import Config
from search_engines.es.documents import TedDocument


def main() -> None:

    es = Elasticsearch(Config.DEV_HOST)
    df = pd.read_csv(PathManager.DATA_DIR / "ted_main.csv")

    for index, line in tqdm(df.iterrows()):
        doc: TedDocument = {
            "comments": line["comments"],
            "description": line["description"],
            "duration": line["duration"],
            "published_date": line["published_date"],
            "ratings": line["ratings"],
            "created_at": datetime.now()
        }
        es.create(index='ted', id=index, body=doc)


if __name__ == '__main__':
    main()
