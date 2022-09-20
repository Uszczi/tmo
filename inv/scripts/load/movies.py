import os
import re
from dataclasses import dataclass
from datetime import date

from inv.db import get_db
from inv.repo.movie import MovieRepo

db = get_db()


def get_example_data_paths():
    path = "example_data/films"
    files = os.listdir(path)
    files = sorted(files)
    files = [f"{path}/{file}" for file in files]
    return files


def extract_directors(line: str) -> tuple[str, str]:
    directors = re.findall(r"\*\*.*\*\*", line)
    if not directors:
        raise Exception

    directors = directors[0]
    line = line.removesuffix(directors).strip()

    directors = directors.removesuffix("**").removeprefix("**")
    return line, directors


def extract_production_year(line: str) -> tuple[str, int]:
    production_year = re.findall("\([0-9]*\)", line)
    if not production_year:
        raise Exception

    production_year = production_year[0]
    line = line.removesuffix(production_year).strip()

    production_year = production_year[1:-1]
    return line, int(production_year)


def process_line(line: str, watch_year: int):
    line = line.strip()
    line, directors = extract_directors(line)
    title, production_year = extract_production_year(line)
    watch_date = date(watch_year, 1, 1)

    @dataclass
    class Movie:
        title: str
        production_year: str
        watch_date: str
        directors: str

    movie = Movie(title, production_year, watch_date, directors)
    return movie


async def fill_db_with_movies():
    paths = get_example_data_paths()

    aaa = []
    for path in paths:
        year = int(path[-7:-3])
        with open(path, "r") as f:
            for index, line in enumerate(f.readlines(), start=1):
                if not line:
                    continue
                try:
                    aaa.append(process_line(line, watch_year=year))
                except Exception as e:
                    print(f"Failed for {path} line: {index} {e=}")

    await MovieRepo.create_many(aaa)


if __name__ == "__main__":
    import asyncio

    asyncio.run(fill_db_with_movies())
