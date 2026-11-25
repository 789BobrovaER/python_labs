# ЛР7 — Поиск, сортировка и измерение времени

## Задание A: поиск

### linear_search

```python
def linear_search(nums, x) -> int:
    """Индекс первого вхождения x или -1.

    linear_search([4, 2, 7, 2], 2) -> 1
    linear_search([4, 2, 7, 2], 9) -> -1
    linear_search([], 1) -> -1
    """
    for index, num in enumerate(nums):
        if num == x:
            return index
    return -1
```

- иду по списку циклом и сравниваю каждый элемент с `x`
- возвращаю индекс первого совпадения
- если не нашла, возвращаю `-1`

### binary_search

```python
def binary_search(sorted_nums, x) -> int:
    """Индекс x в отсортированном по возрастанию списке или -1.
    На неотсортированном списке результат не определён.

    binary_search([1, 3, 5, 7], 5) -> 2
    binary_search([1, 3, 5, 7], 4) -> -1
    binary_search([5], 5) -> 0
    binary_search([], 5) -> -1
    """
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] < x:
            lo = mid + 1
        elif sorted_nums[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1
```

- работает только на отсортированном списке
- `lo` и `hi` — границы поиска (индексы), `hi = len - 1` означает последний индекс
- беру середину: если элемент меньше искомого, отбрасываю левую половину, если больше — правую
- когда `lo` стал больше `hi`, искать больше негде, возвращаю `-1`

### two_sum_brute

```python
def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """Пара индексов (i, j), i < j, nums[i] + nums[j] == target, или None.

    two_sum_brute([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_brute([1, 2], 10) -> None
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return None
```

- два вложенных цикла перебирают все пары, сложность O(n²)
- `j` начинается с `i + 1`, чтобы число не складывалось само с собой и пары не повторялись

### two_sum_fast

```python
def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """То же, что two_sum_brute, но за один проход со словарём."""
    seen = {}  # значение -> индекс
    for i, num in enumerate(nums):
        if target - num in seen:
            return seen[target - num], i
        seen[num] = i
    return None
```

- словарь `seen` хранит «значение: его индекс»
- для каждого числа проверяю, видела ли я уже `target - num`; поиск по ключу в словаре быстрый, сложность O(n)
- если не видела, записываю число и его индекс в словарь

## Задание B: сортировки

### bubble_sort

```python
def bubble_sort(nums) -> list:
    """Новый список, отсортированный по возрастанию. Исходный не меняется.

    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    nums2 = list(nums)
    n = len(nums2)
    for i in range(n):
        changed = False
        for j in range(n - i - 1):
            if nums2[j] > nums2[j + 1]:
                nums2[j], nums2[j + 1] = nums2[j + 1], nums2[j]
                changed = True
        if not changed:
            break
    return nums2
```

- делаю копию списка, чтобы исходный не изменился
- за проход сравниваю соседей и меняю местами, если они стоят не по порядку; максимум «всплывает» в конец
- флаг `changed`: если за проход не было обменов, список уже отсортирован, выхожу через `break`

### insertion_sort

```python
def insertion_sort(nums) -> list:
    """Тот же контракт, что у bubble_sort."""
    nums2 = list(nums)
    for i in range(1, len(nums2)):
        t = nums2[i]
        j = i
        while j > 0 and nums2[j - 1] > t:
            nums2[j] = nums2[j - 1]
            j -= 1
        nums2[j] = t
    return nums2
```

- запоминаю очередной элемент `t`
- цикл `while` сдвигает вправо все элементы, которые больше `t`
- как только нашла место, ставлю `t` на него

### selection_sort

```python
def selection_sort(nums) -> list:
    """Тот же контракт, что у bubble_sort."""
    nums2 = list(nums)
    n = len(nums2)
    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            if nums2[j] < nums2[min_pos]:
                min_pos = j
        if min_pos != i:
            nums2[i], nums2[min_pos] = nums2[min_pos], nums2[i]
    return nums2
```

- слева отсортированная часть, справа нет
- на каждом шаге ищу минимум в неотсортированной части и ставлю его на место `i`
- обмен делаю один раз за проход

## Задание C: проверка против эталона

### check_sorting

```python
def check_sorting(fn, trials=100) -> None:
    global checks
    for _ in range(trials):
        nums = random_list()
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {original}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список: {original} -> {nums}"
        checks += 1
```

- генерирую 100 случайных списков длиной 0–50, значения от −100 до 100, с повторами
- сравниваю результат со `sorted`
- проверяю, что исходный список не изменился

### check_search

```python
def check_search() -> None:
    global checks
    for _ in range(100):
        nums = random_list()
        x = random.randint(-110, 110)  # x может отсутствовать

        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1
        got = linear_search(nums, x)
        assert got == expected, f"linear_search на {nums}, x={x}: {got}, ожидалось {expected}"

        s = sorted(nums)
        res = binary_search(s, x)
        if x in s:
            assert res != -1 and s[res] == x, f"binary_search на {s}, x={x}: {res}"
        else:
            assert res == -1, f"binary_search нашла отсутствующий x на {s}, x={x}: {res}"

        if s:
            for edge in (s[0], s[-1]):
                r = binary_search(s, edge)
                assert r != -1 and s[r] == edge, f"binary_search не нашла край {edge} в {s}: {r}"
        checks += 1
```

- `linear_search` сравниваю с `list.index`; если числа нет, ловлю `ValueError` и считаю эталоном `-1`
- для бинарного поиска сортирую список
- из-за дубликатов бинарный поиск может вернуть любой индекс, поэтому проверяю, что `s[res] == x`
- отдельно проверяю `x`, которого нет, и крайние элементы

### check_two_sum

```python
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
```

- запускаю оба алгоритма; либо оба вернули `None`, либо оба нашли пару
- у найденной пары проверяю `i < j` и сумму

### Запуск проверки

```
python -m src.lab07.check
```

![alt text](image.png)

## Задание D: замеры

- меряю через `timeit` (`number=1`), данные берутся из `data/samples/lab07/numbers_{n}.csv` и одни и те же отдаются всем алгоритмам
- `random.seed(42)`, чтобы результаты повторялись
- на n = 100 000 квадратичные сортировки не запускаются, в таблице пишется `> 60`
- для бинарного поиска время сортировки вынесено отдельной строкой `sort_once`
- в Two Sum пара гарантированно существует
- таблица печатается в консоль f-строками с выравниванием и сохраняется в `data/lab07/bench.csv`

```
python -m src.lab07.bench
```

![alt text](<Снимок экрана 2026-11-24 212043.png>)

## Таблица бенчмарка

Таблица взята из `data/lab07/bench.csv`. Время в секундах, каждый замер — один запуск (`timeit.timeit(..., number=1)`). Значение `> 60` означает, что алгоритм не запускался.

```python
task,n,impl,seconds
sort,1000,sorted,0.000175
sort,1000,bubble,0.086816
sort,1000,insertion,0.045914
sort,1000,selection,0.038024
sort,10000,sorted,0.002052
sort,10000,bubble,9.447795
sort,10000,insertion,4.994603
sort,10000,selection,4.382503
sort,100000,sorted,0.029155
sort,100000,bubble,> 60
sort,100000,insertion,> 60
sort,100000,selection,> 60
search,100000,linear,4.377276
search,100000,sort_once,0.030073
search,100000,binary,0.058108
two_sum,1000,brute,0.058217
two_sum,1000,fast,0.000261
two_sum,10000,brute,0.24459
two_sum,10000,fast,0.000434

```

## Выводы

**Пузырёк против `sorted`.** Пузырьковая сортировка имеет сложность \(O(n^2)\). Это значит, что при увеличении количества элементов в 10 раз количество операций возрастает примерно в \(10^2=100\) раз.
Функция sorted() использует алгоритм со сложностью \(O(nlog n)\) в среднем и худшем случае. Поэтому увеличение массива в 10 раз приводит к гораздо меньшему увеличению времени работы — примерно в 12 раз.

**Бинарный поиск и сортировка.** Бинарный поиск смотрит в середину и по её значению отбрасывает половину списка. Без сортировки такое отбрасывание не имеет смысла, и x можно пропустить. Поэтому на неотсортированном списке результат не определить. Сортировка стоит O(n log n) и делается один раз; после неё каждый запрос стоит O(log n) вместо O(n). 

**Результат `check.py`.** На первых запусках check.py нашёл расхождения с эталоном: в binary_search границы lo и hi были заданы значениями элементов, а не индексами (на пустом списке возникала ошибка IndexError), а в bubble_sort сравнивались неверные элементы. Я исправила эти места: lo = 0, hi = len(sorted_nums) - 1, в пузырьке сравниваются соседние a[j] и a[j+1]. После исправления все 500 проверок проходят: OK: 500 проверок.

**Two Sum.** При n = 1 000 разница почти незаметна, при n = 10 000 `two_sum_brute` занимает 0.24459 с, а `two_sum_fast` — 0.000434 с. Перебор пар — O(n²), словарь за один проход — O(n).
