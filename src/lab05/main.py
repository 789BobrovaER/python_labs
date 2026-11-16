
from pathlib import Path

from .json_csv import json_to_csv, csv_to_json
from .csv_xlsx import csv_to_xlsx


# Корневая папка проекта
BASE_DIR = Path(__file__).resolve().parents[2]

SAMPLES_DIR = BASE_DIR / "data" / "samples"
OUT_DIR = BASE_DIR / "data" / "out"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Запуск демонстрации ЛР5\n")

    # 1. JSON → CSV
    print("№1: Конвертация JSON в CSV...")

    json_to_csv(
        SAMPLES_DIR / "people.json",
        OUT_DIR / "people_from_json.csv"
    )

    print("Создан: data/out/people_from_json.csv")

    # 2. CSV → JSON
    print("\n№2: Конвертация CSV в JSON...")

    csv_to_json(
        SAMPLES_DIR / "people.csv",
        OUT_DIR / "people_from_csv.json"
    )

    print("Создан: data/out/people_from_csv.json")

    # 3. CSV → XLSX
    print("\n№3: Конвертация CSV в XLSX...")

    csv_to_xlsx(
        SAMPLES_DIR / "people.csv",
        OUT_DIR / "people.xlsx"
    )

    print("Создан: data/out/people.xlsx")

    print("\nВсе демонстрационные сценарии выполнены!")


if __name__ == "__main__":
    main()
