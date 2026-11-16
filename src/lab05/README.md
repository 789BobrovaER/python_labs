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
import csv
import json
from pathlib import Path


def _check_file(path: str | Path, suffix: str) -> Path:
    """Проверяет расширение и существование файла."""
    p = Path(path)
    if p.suffix.lower() != suffix:
        raise ValueError(f"Неверный тип файла: {p.name} (ожидался {suffix})")
    if not p.is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")
    return p


def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    """
    JSON (список словарей) → CSV.
    Отсутствующие поля заполняются пустой строкой.
    Порядок колонок — как в первом объекте (остальные ключи добавляются в конец).
    """
    src = _check_file(json_path, ".json")
    if Path(csv_path).suffix.lower() != ".csv":
        raise ValueError(f"Неверный тип файла: {Path(csv_path).name} (ожидался .csv)")

    with src.open(encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Некорректный JSON: {e}") from e

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not all(isinstance(row, dict) for row in data):
        raise ValueError("Ожидается список словарей")

    fieldnames = list(data[0].keys())
    for row in data[1:]:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)

    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        for row in data:
            writer.writerow({k: ("" if v is None else v) for k, v in row.items()})


def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    """
    CSV (с заголовком) → JSON (список словарей, значения — строки).
    """
    src = _check_file(csv_path, ".csv")
    if Path(json_path).suffix.lower() != ".json":
        raise ValueError(f"Неверный тип файла: {Path(json_path).name} (ожидался .json)")

    with src.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV без заголовка")
        rows = list(reader)

    if not rows:
        raise ValueError("Пустой CSV")

    Path(json_path).parent.mkdir(parents=True, exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
```
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
