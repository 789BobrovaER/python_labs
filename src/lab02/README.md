# Задание №1

## min_max

Если список пуст, вызывается `ValueError`. Иначе первый элемент становится и минимумом (`lo`), и максимумом (`hi`). Цикл проходит по остальным элементам: если число меньше `lo`, обновляем `lo`, если больше `hi`, обновляем `hi`. В конце возвращается кортеж `(lo, hi)`. Встроенные `min()` и `max()` не используются.

<img width="906" height="480" alt="Снимок экрана 2026-10-06 185112" src="https://github.com/user-attachments/assets/73f8142d-996e-44c8-8a8f-c0c0b63274ce" />

<img width="1368" height="121" alt="Снимок экрана 2026-10-06 185203" src="https://github.com/user-attachments/assets/1450fed6-cdc9-4330-b520-01fdc56969be" />

## unique_sorted

`set(nums)` убирает повторы, `list(...)` возвращает результат в список. Затем пузырьковая сортировка: внешний цикл повторяет проходы, внутренний сравнивает соседние элементы и меняет их местами, если левый больше правого. С каждым проходом самое большое число уходит в конец, поэтому отсортированный хвост пропускается (`len(sp) - 1 - i`). Встроенные `sorted()` и `sort()` не используются.

<img width="991" height="351" alt="Снимок экрана 2026-10-06 185357" src="https://github.com/user-attachments/assets/1b6707ce-f7be-412d-b52c-c1face3cdb1a" />

<img width="1362" height="121" alt="Снимок экрана 2026-10-06 185425" src="https://github.com/user-attachments/assets/6fc90037-869b-4f28-9c55-c04b6fcd41e9" />

## flatten

Создаём пустой `result`. Цикл `for row in mat` берёт каждую строку матрицы. Если `row` не список и не кортеж, вызывается `TypeError` с названием полученного типа. Иначе вложенный цикл добавляет элементы строки в `result` по одному. Получается плоский список по строкам (row-major), пустые строки ничего не добавляют.

<img width="1222" height="402" alt="Снимок экрана 2026-10-06 185619" src="https://github.com/user-attachments/assets/33c871f9-8bfd-4e34-87b5-a60b3fff7d93" />

<img width="1356" height="111" alt="Снимок экрана 2026-10-06 185640" src="https://github.com/user-attachments/assets/e2639e8a-efb0-42e1-9998-8defba7fcc3f" />


# Задание №2
## вспомогательная функция check

Проверяет, что матрица прямоугольная. Длина первой строки сохраняется в `ln`, и с ней через `all(...)` сравниваются длины всех строк. Если хотя бы одна отличается, вызывается `ValueError`, иначе функция возвращает `True`. Эту проверку используют все функции ниже.


<img width="728" height="140" alt="Снимок экрана 2026-10-04 210609" src="https://github.com/user-attachments/assets/3a7902fb-23f7-4be6-97d5-b7a3c30cbe75" />

## transpose

Для пустой матрицы сразу возвращается `[]`, затем `check` проверяет прямоугольность. Создаётся `tr_mat` с `ln` пустыми строками (по одной на каждый столбец). Затем для каждого номера столбца `l` элемент `m[l]` из каждой строки `m` добавляется в `tr_mat[l]`. Так строки и столбцы меняются местами.

<img width="868" height="549" alt="Снимок экрана 2026-10-06 190735" src="https://github.com/user-attachments/assets/5fa90ccb-88b4-4841-b0e5-b85a3bc5bae2" />
<img width="918" height="119" alt="Снимок экрана 2026-10-06 190751" src="https://github.com/user-attachments/assets/f28cf8ac-80d1-4ee1-bcfe-74f0c8c727cd" />





## row_sums

Для пустой матрицы возвращается `[]`, затем `check` проверяет прямоугольность. Генератор списка `[sum(m) for m in mat]` считает сумму каждой строки и собирает суммы в один список.

<img width="760" height="292" alt="Снимок экрана 2026-10-06 191106" src="https://github.com/user-attachments/assets/1ce1433f-c239-46aa-8ba9-b7ce50c845d8" />
<img width="868" height="102" alt="Снимок экрана 2026-10-06 191122" src="https://github.com/user-attachments/assets/6f6cbcd7-3990-4bce-9b7c-40e5dd37abb4" />




## col_sums

Для пустой матрицы возвращается `[]`, затем `check` проверяет прямоугольность. Внешний цикл идёт по номерам столбцов `l`. Для каждого столбца `s` обнуляется, и в неё складываются элементы `m[l]` из всех строк. Готовая сумма добавляется в список `col`.


<img width="794" height="437" alt="Снимок экрана 2026-10-06 191312" src="https://github.com/user-attachments/assets/870dfc8a-a6b9-491a-95d3-a1304064f5d7" />
<img width="824" height="93" alt="Снимок экрана 2026-10-06 191335" src="https://github.com/user-attachments/assets/4d1e0da9-8fb3-4bcc-a3dd-4c5d0ba6e573" />





# Задание №3

Кортеж распаковывается на `fio`, `group` и `gpa`. `split()` делит ФИО на слова и убирает лишние пробелы (для группы это делает `" ".join(group.split())`). Если ФИО или группа пустые либо GPA вне диапазона 0–5, вызывается `ValueError`. Фамилия остаётся первым словом, а из имени и отчества (`fio[1:3]`) берутся первые буквы в верхнем регистре с точками, поэтому функция работает и с двумя, и с тремя словами. GPA форматируется с двумя знаками после запятой (`:.2f`), и всё собирается в строку вида `Иванов И.И., гр. BIVT-25, GPA 4.60`.

<img width="1316" height="522" alt="Снимок экрана 2026-10-06 162736" src="https://github.com/user-attachments/assets/39db417b-a513-40ac-81d5-c278bc3344fa" />
<img width="415" height="48" alt="image" src="https://github.com/user-attachments/assets/bbf248f8-cf26-414a-a07d-2fc101baaaf0" />



<img width="971" height="39" alt="Снимок экрана 2026-10-04 211211" src="https://github.com/user-attachments/assets/9855c6b9-e198-4427-b59d-e0b508e446ba" />
<img width="427" height="58" alt="Снимок экрана 2026-10-04 211224" src="https://github.com/user-attachments/assets/c19ae980-1899-402b-8365-68e78f2f8f43" />

