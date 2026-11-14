# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике

Цель: закрепить работу с файлами (чтение/запись, кодировки), автоматизировать сбор статистики по словам и выгружать её в CSV.

## Задание A

Модуль `src/lab04/io_txt_csv.py` с типами и докстрингами:

- `ensure_parent_dir`: создаёт родительскую папку файла, если её нет.
- `read_text`: читает файл целиком в строку (по умолчанию UTF-8, другая кодировка, например `encoding="cp1251"`, описана в докстринге). `FileNotFoundError` и `UnicodeDecodeError` не перехватываются.
- `write_csv`: проверяет, что все строки одной длины (иначе `ValueError`), и пишет CSV с разделителем `,`.

Краевые случаи: пустой файл читается как `""`; `write_csv` без данных создаёт пустой файл, только с `header` создаёт файл из одной строки заголовка. Файл читается целиком (по ТЗ), для больших файлов в реальности лучше читать построчно.




## Задание B

Скрипт `src/lab04/text_report.py` (`argparse`):

1. Читает входной файл (по умолчанию `data/lab04/input.txt`).
2. Нормализует, токенизирует и считает частоты (`normalize`, `tokenize`, `count_freq` из ЛР3).
3. Сортирует: частота ↓, слово ↑.
4. Сохраняет `data/lab04/report.csv` с колонками `word,count`. Пустой вход даёт отчёт только с заголовком.
5. Печатает в консоль: всего слов, уникальных слов, топ-5.

Ошибки (нет файла, не та кодировка): сообщение в stderr и код выхода `1`. Другая кодировка: `--encoding cp1251`.

```
python -m src.lab04.text_report
```
<img width="308" height="134" alt="Снимок экрана 2026-11-14 233006" src="https://github.com/user-attachments/assets/994af9fc-76fa-4c20-a203-58917d4b14ae" />
<img width="550" height="318" alt="Снимок экрана 2026-11-14 233001" src="https://github.com/user-attachments/assets/8a4401e2-b1bd-459b-9aaa-1dbe66a141ef" />



## ★ Дополнительно

- Несколько файлов через `--in`: частоты по каждому файлу и сводные.
- `report_per_file.csv` (`file,word,count`; сортировка `file` ↑, `count` ↓, `word` ↑) и `report_total.csv` (`word,count`).
- Флаг `--table`: топ-5 таблицей с автоматической шириной колонки.

```
python -m src.lab04.text_report --in data/lab04/a.txt data/lab04/b.txt --per-file data/lab04/report_per_file.csv --total data/lab04/report_total.csv --table
```
<img width="1373" height="464" alt="Снимок экрана 2026-11-14 233527" src="https://github.com/user-attachments/assets/8c77f765-2918-433d-a222-b3f9775845a4" />


