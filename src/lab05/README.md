# ЛР5 — JSON и конвертации (JSON ↔ CSV, CSV → XLSX)

## Цель работы

Изучение формата JSON, сериализации и десериализации данных, а также реализация конвертации между JSON, CSV и XLSX.


## Реализованные функции

### 1. JSON → CSV

Функция `json_to_csv(json_path, csv_path)`:

- преобразует список словарей JSON в CSV;
- формирует заголовки на основе ключей объектов;
- заполняет отсутствующие значения пустыми строками;
- использует кодировку UTF-8.
```python
[
    {
        "destination": "Paris",
        "country": "France",
        "days": "5",
        "budget": "120000"
    },
    {
        "destination": "Tokyo",
        "country": "Japan",
        "days": "10",
        "budget": "250000"
    },
    {
        "destination": "Rome",
        "country": "Italy",
        "days": "4",
        "budget": "95000"
    },
    {
        "destination": "Istanbul",
        "country": "Turkey",
        "days": "7"
    },
    {
        "destination": "Prague",
        "country": "Czech Republic",
        "days": "3",
        "budget": "70000"
    }
]
```
<img width="442" height="167" alt="изображение" src="https://github.com/user-attachments/assets/e007defb-6f52-4c5b-b6fe-13e8e5590e22" />

### 2. CSV → JSON

Функция `csv_to_json(csv_path, json_path)`:

- преобразует CSV в список словарей JSON;
- использует первую строку CSV как заголовки;
- сохраняет значения в виде строк;
- форматирует JSON с отступами.

### 3. CSV → XLSX

Функция `csv_to_xlsx(csv_path, xlsx_path)`:

- преобразует CSV в XLSX;
- создаёт лист Sheet1;
- использует первую строку как заголовок;
- автоматически рассчитывает ширину колонок (не менее 8 символов).
```python
"""CSV → XLSX"""

import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Первая строка — заголовок, лист "Sheet1", автоширина колонок (≥ 8).
    """
    src = Path(csv_path)
    if not src.is_file():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with src.open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))

    if not rows or not any(rows):
        raise ValueError("Пустой CSV")
    if not rows[0]:
        raise ValueError("CSV без заголовка")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    widths = [0] * len(rows[0])
    for i, row in enumerate(rows):
        # выравниваем длину строк по количеству колонок заголовка
        row = list(row) + [""] * (len(widths) - len(row))
        ws.append(row[: len(widths)])
        for j, value in enumerate(row[: len(widths)]):
            widths[j] = max(widths[j], len(str(value)))

    for j, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(j)].width = max(w + 2, 8)

    Path(xlsx_path).parent.mkdir(parents=True, exist_ok=True)
    wb.save(xlsx_path)

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parents[2]
    SAMPLES_DIR = BASE_DIR / "data" / "samples"
    OUT_DIR = BASE_DIR / "data" / "out"
    
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Тест Задания Б (CSV -> XLSX)")
    
    input_file = SAMPLES_DIR / "cities.csv"
    output_file = OUT_DIR / "people.xlsx"
    
    print(f"Конвертация {input_file} в {output_file}")
    csv_to_xlsx(input_file, output_file)
    print("Успешно.")
```
## Используемые библиотеки

- `json`, `csv`, `pathlib` — стандартные библиотеки Python.
- `openpyxl` — создание Excel-файлов.

Установка зависимости:

```bash
pip install -r requirements.txt
```

## Запуск программы

Активировать виртуальное окружение:

```powershell
.venv\Scripts\activate
```

Установить зависимости:

```bash
python -m pip install -r requirements.txt
```

Запустить демонстрационные сценарии:

```bash
python -m src.lab05.main
```

## Тестовые сценарии

1. JSON → CSV: проверка заголовков и количества записей.
2. CSV → JSON: проверка ключей, количества объектов и строковых значений.
3. CSV → XLSX: проверка структуры таблицы, названия листа и ширины колонок.
4. Проверка обработки ошибок: отсутствующие файлы, неверные расширения, пустые входные данные и неподдерживаемая структура JSON.

## Допущения

- Входной JSON должен представлять собой непустой список словарей.
- В CSV первая строка содержит заголовки.
- Все файлы читаются и записываются в кодировке UTF-8.
- Значения при преобразовании CSV → JSON сохраняются как строки.
- При преобразовании JSON → CSV отсутствующие поля заполняются пустыми строками.
- Пути к файлам задаются относительно корневой папки проекта.

## Результаты выполнения

Скриншоты выполнения и проверки XLSX находятся в папке `images/lab05/`.
