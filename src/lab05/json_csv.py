import csv
import json
from pathlib import Path


def _check_exists(path: str) -> Path:
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")
    return p


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    JSON (список словарей) → CSV.
    Отсутствующие поля заполняются пустой строкой.
    Порядок колонок — как в первом объекте (остальные ключи добавляются в конец).
    """
    src = _check_exists(json_path)

    with src.open(encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Некорректный JSON: {e}") from e

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not all(isinstance(row, dict) for row in data):
        raise ValueError("Ожидается список словарей")

    # Порядок колонок: сначала ключи первого объекта, затем новые по порядку появления
    fieldnames = list(data[0].keys())
    for row in data[1:]:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)

    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow({k: ("" if row.get(k) is None else row.get(k, "")) for k in fieldnames})


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    CSV (с заголовком) → JSON (список словарей, значения — строки).
    """
    src = _check_exists(csv_path)

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

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parents[2]
    SAMPLES_DIR = BASE_DIR / "data" / "samples"
    OUT_DIR = BASE_DIR / "data" / "out"
    
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Тест Задания А (JSON <-> CSV)")
    
    # Тест 1: JSON -> CSV
    print(f"1. Конвертация {SAMPLES_DIR / 'people.json'} в {OUT_DIR / 'people_from_json.csv'}")
    json_to_csv(SAMPLES_DIR / "people.json", OUT_DIR / "people_from_json.csv")
    print("   Успешно.")
    
    # Тест 2: CSV -> JSON
    print(f"2. Конвертация {SAMPLES_DIR / 'people.csv'} в {OUT_DIR / 'people_from_csv.json'}")
    csv_to_json(SAMPLES_DIR / "people.csv", OUT_DIR / "people_from_csv.json")
    print("   Успешно.")