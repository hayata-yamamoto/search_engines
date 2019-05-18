from setuptools import setup, find_packages
from typing import IO


def main() -> None:
    f: IO
    with open("requirements.txt", 'r') as f:
        req = f.read().splitlines()

    setup(
        name="search_engines",
        version="0.0.1",
        packages=find_packages(exclude=['search_engines/data']),
        install_requires=req
    )


if __name__ == '__main__':
    main()
