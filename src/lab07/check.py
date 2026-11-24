import random
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

checks = 0  # общий счётчик проверок для "OK: N проверок"


def random_list() -> list:
    """Список длиной 0..50, значения -100..100, с повторами."""
    return [random.randint(-100, 100) for _ in range(random.randint(0, 50))]


def check_sorting(fn, trials=100) -> None:
    global checks
    for _ in range(trials):
        nums = random_list()
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {original}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список: {original} -> {nums}"
        checks += 1


def check_search() -> None:
    global checks
    for _ in range(100):
        nums = random_list()
        x = random.randint(-110, 110)  # x может отсутствовать

        # linear_search против list.index (-1 против ValueError)
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1
        got = linear_search(nums, x)
        assert got == expected, f"linear_search на {nums}, x={x}: {got}, ожидалось {expected}"

        # binary_search на отсортированном; при дубликатах индекс любой, но s[res] == x
        s = sorted(nums)
        res = binary_search(s, x)
        if x in s:
            assert res != -1 and s[res] == x, f"binary_search на {s}, x={x}: {res}"
        else:
            assert res == -1, f"binary_search нашла отсутствующий x на {s}, x={x}: {res}"

        # крайние элементы
        if s:
            for edge in (s[0], s[-1]):
                r = binary_search(s, edge)
                assert r != -1 and s[r] == edge, f"binary_search не нашла край {edge} в {s}: {r}"
        checks += 1


def check_two_sum(trials=100) -> None:
    global checks
    for _ in range(trials):
        nums = random_list()
        target = random.randint(-200, 200)
        a = two_sum_brute(nums, target)
        b = two_sum_fast(nums, target)
        assert (a is None) == (b is None), \
            f"two_sum разошлись на {nums}, target={target}: brute={a}, fast={b}"
        for name, res in (("brute", a), ("fast", b)):
            if res is not None:
                i, j = res
                assert i < j and nums[i] + nums[j] == target, \
                    f"two_sum_{name}: пара {res} не подходит на {nums}, target={target}"
        checks += 1


if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print(f"OK: {checks} проверок")