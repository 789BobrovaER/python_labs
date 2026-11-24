import csv
import os
import random
import timeit
from src.lab04.io_txt_csv import write_csv
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

QUADRATIC_LIMIT = 10_000  # квадратичные сортировки на большем n не запускаем


def read_numbers(path):
    with open(path, encoding="utf-8") as f:
        return [int(row["value"]) for row in csv.DictReader(f)]


def get_numbers(n):
    """Данные из data/samples/lab07/numbers_{n}.csv; если файла нет — создаём (seed 42)."""
    path = f"data/samples/lab07/numbers_{n}.csv"
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        rnd = random.Random(42)
        with open(path, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["value"])
            for _ in range(n):
                w.writerow([rnd.randint(-10**6, 10**6)])
    return read_numbers(path)


def bench_sorts(n):
    data = get_numbers(n)
    rows = []
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", t))
    for name, fn in (("bubble", bubble_sort),
                     ("insertion", insertion_sort),
                     ("selection", selection_sort)):
        if n > QUADRATIC_LIMIT:
            rows.append(("sort", n, name, "> 60"))
        else:
            t = timeit.timeit(lambda: fn(data), number=1)
            rows.append(("sort", n, name, t))
    return rows


def bench_search(n=100_000, queries=10_000):
    data = get_numbers(n)
    rnd = random.Random(42)
    qs = [rnd.randint(-10**6, 10**6) for _ in range(queries)]
    rows = []

    t = timeit.timeit(lambda: [linear_search(data, q) for q in qs], number=1)
    rows.append(("search", n, "linear", t))

    # бинарному нужна сортировка — время сортировки отдельной строкой
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("search", n, "sort_once", t))
    sdata = sorted(data)
    t = timeit.timeit(lambda: [binary_search(sdata, q) for q in qs], number=1)
    rows.append(("search", n, "binary", t))
    return rows


def bench_two_sum(n):
    data = get_numbers(n)
    target = data[-2] + data[-1]  # пара гарантированно существует (в конце списка)
    rows = []
    for name, fn in (("brute", two_sum_brute), ("fast", two_sum_fast)):
        t = timeit.timeit(lambda: fn(data, target), number=1)
        rows.append(("two_sum", n, name, t))
    return rows


def print_table(rows):
    print(f"{'task':<10}{'n':>9}  {'impl':<12}{'seconds':>12}")
    print("-" * 45)
    for task, n, impl, sec in rows:
        sec_s = f"{sec:.6f}" if isinstance(sec, float) else str(sec)
        print(f"{task:<10}{n:>9}  {impl:<12}{sec_s:>12}")


def main():
    random.seed(42)
    rows = []
    for n in (1_000, 10_000, 100_000):
        rows += bench_sorts(n)
    rows += bench_search()
    for n in (1_000, 10_000):
        rows += bench_two_sum(n)

    rows = [(t, n, i, round(s, 6) if isinstance(s, float) else s) for t, n, i, s in rows]
    print_table(rows)
    os.makedirs("data/lab07", exist_ok=True)
    write_csv(rows, "data/lab07/bench.csv", header=("task", "n", "impl", "seconds"))


if __name__ == "__main__":
    main()