# Лабораторная 4 — Файлы: TXT/CSV и отчёты по текстовой статистике

**Цель:** закрепить работу с файлами (чтение/запись, кодировки), автоматизировать сбор статистики по словам и выгружать её в CSV.
Используется `src/lib/text.py` из ЛР3 (`normalize`, `tokenize`, `count_freq`, `top_n`). Только стандартная библиотека.

## Структура

```
src/lab04/io_txt_csv.py     # read_text, write_csv, ensure_parent_dir
src/lab04/text_report.py    # отчёт по частотам (+ ★)
data/lab04/                 # input.txt, a.txt, b.txt
images/lab04/               # скриншоты запусков
```

Все команды запускаются **из корня репозитория** (через `-m`, чтобы работали импорты `src.…`).

## Задание A — `io_txt_csv.py`

- `read_text(path, encoding="utf-8") -> str` — читает файл целиком. `FileNotFoundError` и `UnicodeDecodeError` не перехватываются. Другая кодировка: `read_text("old.txt", encoding="cp1251")`.
- `write_csv(rows, path, header=None)` — пишет CSV (разделитель `,`), заголовок первой строкой. Если длины строк разные — `ValueError`; проверка идёт **до** открытия файла, поэтому старый файл не затирается.
- `ensure_parent_dir(path)` — создаёт родительские папки (вызывается внутри `write_csv`).

Мини-тест:

```python
from src.lab04.io_txt_csv import read_text, write_csv
txt = read_text("data/lab04/input.txt")
write_csv([("word", "count"), ("test", 3)], "data/lab04/check.csv")
```

Краевые случаи: пустой файл → `""`; `write_csv([], p)` → пустой файл; `write_csv([], p, header=("a","b"))` → только `a,b`.
Файл читается целиком (по ТЗ); в реальных задачах с большими файлами стоит читать построчно.

## Задание B — `text_report.py`

```
python -m src.lab04.text_report
python -m src.lab04.text_report --in data/lab04/input.txt --out data/lab04/report.csv
python -m src.lab04.text_report --in data/lab04/input.txt --encoding cp1251
```

| Параметр | По умолчанию | Смысл |
|---|---|---|
| `--in`, `-i` | `data/lab04/input.txt` | один или несколько входных файлов |
| `--out`, `-o` | `data/lab04/report.csv` | основной отчёт `word,count` |
| `--encoding`, `-e` | `utf-8` | кодировка входов |
| `--per-file` | — | ★ отчёт `file,word,count` |
| `--total` | — | ★ сводный отчёт `word,count` |
| `--table` | — | ★ топ-5 таблицей |

Сортировка: `count ↓`, затем `word ↑`. В консоль: `Всего слов`, `Уникальных слов`, `Топ-5`.

**Политика ошибок:** файла нет или кодировка не подошла → сообщение в stderr и код выхода `1` (без traceback).
**Политика пустого входа:** `report.csv` содержит только заголовок `word,count`; в консоль выводится `Всего слов: 0`.

## Тест-кейсы

| # | Вход | Команда | Результат |
|---|---|---|---|
| A | `Привет, мир! Привет!!!` | `python -m src.lab04.text_report` | `привет,2` / `мир,1`; всего 3, уникальных 2 |
| B | пустой файл | `--in data/lab04/empty.txt` | только `word,count`; всего 0 |
| C | `Привет` в cp1251 | с `--encoding cp1251` | `привет,1`; без флага — ошибка кодировки, exit 1 |
| D★ | `a.txt`: `Привет мир`, `b.txt`: `Привет, привет!` | `--in data/lab04/a.txt data/lab04/b.txt --per-file data/lab04/report_per_file.csv --total data/lab04/report_total.csv` | см. ниже |

`report_per_file.csv` (сортировка `file ↑, count ↓, word ↑`, поэтому `мир` раньше `привет` в `a.txt`):

```
file,word,count
a.txt,мир,1
a.txt,привет,1
b.txt,привет,2
```

`report_total.csv`:

```
word,count
привет,3
мир,1
```

Скриншоты: `images/lab04/img01.png` … `img05.png`.