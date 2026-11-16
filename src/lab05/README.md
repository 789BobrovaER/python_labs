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
<img width="312" height="185" alt="Снимок экрана 2026-11-16 205411" src="https://github.com/user-attachments/assets/682893d6-6318-45d0-81b0-443bfd02d5d6" />

```python
[
  {
    "name": "Alice",
    "age": "22",
    "city": "SPB"
  },
  {
    "name": "Bob",
    "age": "25",
    "city": "Moscow"
  },
  {
    "name": "Carlos",
    "age": "30",
    "city": "Kazan"
  },
  {
    "name": "Dana",
    "age": "21",
    "city": "SPB"
  },
  {
    "name": "Andrey",
    "age": "27",
    "city": "Novosibirsk"
  }
]
```

### 3. CSV → XLSX

Функция `csv_to_xlsx(csv_path, xlsx_path)`:

- преобразует CSV в XLSX;
- создаёт лист Sheet1;
- использует первую строку как заголовок;
- автоматически рассчитывает ширину колонок (не менее 8 символов).
<img width="350" height="193" alt="изображение" src="https://github.com/user-attachments/assets/9da00ea5-deb4-4f30-8e74-51ef4b1737ad" />
<img width="366" height="211" alt="изображение" src="https://github.com/user-attachments/assets/bb2af605-40e5-49d4-9f1b-6066c9d789c0" />

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

<img width="472" height="423" alt="изображение" src="https://github.com/user-attachments/assets/522ab8a8-cb44-467d-a927-6634ca6c8fd8" />
