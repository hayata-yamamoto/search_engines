from pathlib import Path


class PathManager:
    ROOT_DIR: Path = Path(__file__).resolve().parents[2]
    DATA_DIR: Path = ROOT_DIR / "data"
    BASE_DIR: Path = ROOT_DIR / "search_engines"
    CORE: Path = BASE_DIR / "core"
    ES: Path = BASE_DIR / "es"
