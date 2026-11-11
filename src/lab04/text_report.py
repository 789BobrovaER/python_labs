"""Отчёт по частотам слов: читает TXT-файл(ы), пишет CSV, печатает резюме."""

import argparse
import sys
from collections import Counter
from pathlib import Path

from io_txt_csv import read_text, write_csv
from src.lib.text import count_freq, normalize, tokenize, top_n


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортирует пары (слово, частота): частота по убыванию, слово по алфавиту."""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def print_table(rows: list[tuple[str, int]]) -> None:
    """Печатает пары (слово, частота) таблицей с шириной по самому длинному слову."""
    if not rows:
        return
    width = max(len("слово"), *(len(w) for w, _ in rows))
    print(f"{'слово':<{width}} | частота")
    print("-" * width + "-+-" + "-" * 7)
    for word, count in rows:
        print(f"{word:<{width}} | {count}")


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
    p.add_argument("--table", action="store_true",
                   help="печатать топ-5 таблицей (★)")
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

        tokens = tokenize(normalize(text))
        freq = count_freq(tokens)
        all_tokens += len(tokens)
        total.update(freq)
        name = Path(path).name
        per_file_rows.extend((name, w, c) for w, c in freq.items())

    rows = sorted_word_counts(dict(total))
    write_csv(rows, args.out_file, header=("word", "count"))

    if args.total:
        write_csv(rows, args.total, header=("word", "count"))
    if args.per_file:
        per_file_rows.sort(key=lambda r: (r[0], -r[2], r[1]))
        write_csv(per_file_rows, args.per_file, header=("file", "word", "count"))

    print(f"Всего слов: {all_tokens}")
    print(f"Уникальных слов: {len(total)}")
    print("Топ-5:")
    top = top_n(dict(total), 5)
    if args.table:
        print_table(top)
    else:
        for word, count in top:
            print(f"{word}:{count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())