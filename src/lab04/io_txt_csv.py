"""Ввод/вывод для ЛР4: чтение TXT и запись CSV."""

import csv
from collections.abc import Iterable, Sequence
from pathlib import Path


def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские папки для пути, если их ещё нет.

    Пример: для "data/lab04/out.csv" создаст "data/lab04".
    Если папки уже существуют, ничего не происходит.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает файл целиком и возвращает его содержимое одной строкой.

    Args:
        path: путь к текстовому файлу.
        encoding: кодировка файла, по умолчанию "utf-8". Чтобы выбрать
            другую кодировку, передайте её явно, например:
            ``read_text("old.txt", encoding="cp1251")``.

    Returns:
        Содержимое файла. Для пустого файла возвращается "".

    Raises:
        FileNotFoundError: файла по указанному пути нет.
        UnicodeDecodeError: файл не удалось расшифровать в этой кодировке.
    """
    return Path(path).read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    """Создаёт или перезаписывает CSV-файл с разделителем ",".

    Args:
        rows: строки таблицы (каждая строка - tuple или list).
        path: путь к выходному файлу (папки создаются автоматически).
        header: необязательный заголовок, пишется первой строкой.

    Raises:
        ValueError: если строки в rows имеют разную длину.
    """
    rows = list(rows)
    if rows:
        expected = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != expected:
                raise ValueError(
                    f"Строка {i} имеет длину {len(row)}, ожидалось {expected}"
                )

    ensure_parent_dir(path)
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)