"""Отчёт по частотам слов: читает TXT-файл(ы), пишет CSV, печатает таблицы и резюме."""

import argparse
import sys
from collections import Counter
from pathlib import Path

# корень проекта в sys.path, чтобы работал запуск и кнопкой, и через -m
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.lab04.io_txt_csv import read_text, write_csv  # noqa: E402
from src.lib.text import count_freq, normalize, tokenize, top_n  # noqa: E402


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортирует пары (слово, частота): частота по убыванию, слово по алфавиту."""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def print_table(header: tuple[str, ...], rows: list[tuple]) -> None:
    """Печатает таблицу, ширина каждой колонки равна самому длинному значению."""
    cells = [[str(c) for c in row] for row in rows]
    widths = [
        max(len(h), *(len(r[i]) for r in cells)) if cells else len(h)
        for i, h in enumerate(header)
    ]

    def line(values: list[str]) -> str:
        return " | ".join(v.ljust(w) for v, w in zip(values, widths)).rstrip()

    last = len(widths) - 1
    sep = "+".join(
        "-" * (w + (1 if i in (0, last) else 2)) for i, w in enumerate(widths)
    )
    print(line(list(header)))
    print(sep)
    for r in cells:
        print(line(r))


def parse_args() -> argparse.Namespace:
    """Разбирает аргументы командной строки."""
    p = argparse.ArgumentParser(description="Отчёт по частотам слов (TXT -> CSV)")
    p.add_argument("--in", "-i", dest="inputs", nargs="+",
                   default=["data/lab04/input.txt"],
                   help="входные файлы (по умолчанию data/lab04/input.txt)")
    p.add_argument("--out", "-o", dest="out_file", default="data/lab04/report.csv",
                   help="основной отчёт word,count (по умолчанию data/lab04/report.csv)")
    p.add_argument("--encoding", "-e", default="utf-8",
                   help="кодировка входных файлов, например cp1251")
    p.add_argument("--per-file", dest="per_file", default=None,
                   help="путь для отчёта file,word,count по каждому файлу (★)")
    p.add_argument("--total", default=None,
                   help="путь для сводного отчёта word,count по всем файлам (★)")
    return p.parse_args()


def main() -> int:
    """Точка входа. Возвращает 0 при успехе и 1 при ошибке чтения файла."""
    args = parse_args()

    per_file_rows: list[tuple[str, str, int]] = []
    total: Counter[str] = Counter()
    all_tokens = 0

    for path in args.inputs:
        try:
            text = read_text(path, encoding=args.encoding)
        except FileNotFoundError:
            print(f"Ошибка: файл не найден: {path}", file=sys.stderr)
            return 1
        except UnicodeDecodeError:
            print(f"Ошибка: не удалось прочитать {path} в кодировке "
                  f"{args.encoding} (попробуйте --encoding cp1251)", file=sys.stderr)
            return 1

        # normalize из ЛР3 падает на пустой строке, поэтому пустой вход обрабатываем отдельно
        tokens = tokenize(normalize(text)) if text.strip() else []
        freq = count_freq(tokens)
        all_tokens += len(tokens)
        total.update(freq)
        name = Path(path).name
        per_file_rows.extend((name, w, c) for w, c in freq.items())

    rows = sorted_word_counts(dict(total))
    per_file_rows.sort(key=lambda r: (r[0], -r[2], r[1]))

    write_csv(rows, args.out_file, header=("word", "count"))
    if args.total:
        write_csv(rows, args.total, header=("word", "count"))
    if args.per_file:
        write_csv(per_file_rows, args.per_file, header=("file", "word", "count"))

    if args.per_file:
        print("--- Отчёт по каждому файлу ---")
        print_table(("file", "word", "count"), per_file_rows)
        print()

    title = "Сводный отчёт" if (len(args.inputs) > 1 or args.total) else "Отчёт"
    print(f"--- {title} ---")
    print_table(("word", "count"), rows)
    print()

    print("=== Краткое резюме ===")
    print(f"Всего слов: {all_tokens}")
    print(f"Уникальных слов: {len(total)}")
    print("Топ-5:")
    # top_n из ЛР3 падает на пустом словаре, поэтому пустой случай обходим отдельно
    top = top_n(dict(total), 5) if total else []
    for word, count in top:
        print(f"{word}:{count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())