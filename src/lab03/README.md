## Задание A - text.py
# `normalize`
Приводит текст к единому виду. Проверяет, что на входе строка (иначе TypeError), переводит в нижний регистр через casefold() или lower(), при yo2e=True заменяет «ё» на «е», убирает пробелы по краям и схлопывает любые пробельные символы (\n, \t, \r) в один пробел. Пустая строка вызывает ValueError.
<img width="954" height="500" alt="Снимок экрана 2026-10-20 223240" src="https://github.com/user-attachments/assets/ff781383-e4a4-46df-b74d-65671d34d41f" />
<img width="504" height="86" alt="Снимок экрана 2026-10-20 223255" src="https://github.com/user-attachments/assets/3020a427-8fc9-4c53-bc19-1ae2c4192437" />

# `tokenize`
Разбивает текст на слова. Сначала вызывает normalize, затем регулярное выражение \w+(?:-\w+)* находит последовательности букв, цифр и _, допуская дефис внутри слова (по-настоящему). Знаки препинания и эмодзи отбрасываются, числа считаются словами.
<img width="925" height="294" alt="Снимок экрана 2026-10-20 223313" src="https://github.com/user-attachments/assets/809f1f54-ba21-4b27-a541-ebb3cdc8e5da" />
<img width="568" height="112" alt="Снимок экрана 2026-10-20 223328" src="https://github.com/user-attachments/assets/69c94595-09b7-467a-a91b-11120938bf31" />

# `count_freq`
Считает частоты. Проверяет, что на входе список строк, затем проходит по токенам и увеличивает счётчик в словаре {слово: количество}.
<img width="979" height="455" alt="Снимок экрана 2026-10-20 223347" src="https://github.com/user-attachments/assets/afd4abd4-6a8e-4a7d-85ab-1e7f4e2c8a8a" />
<img width="635" height="52" alt="Снимок экрана 2026-10-20 223400" src="https://github.com/user-attachments/assets/9961fbc9-356c-4f17-97ff-703829311bd0" />

# `top_n`
Выбирает n самых частых слов. Проверяет, что словарь не пустой, сортирует пары по ключу (-частота, слово), то есть по убыванию частоты, а при равенстве по алфавиту, и берёт срез [:n].
<img width="976" height="316" alt="Снимок экрана 2026-10-20 223423" src="https://github.com/user-attachments/assets/6985afcf-739e-426c-9781-42a859e4efce" />
<img width="626" height="53" alt="Снимок экрана 2026-10-20 223431" src="https://github.com/user-attachments/assets/46a41d75-0195-4ac0-9f3b-543303e8a7af" />

## Задание B — src/text_stats.py

Скрипт читает одну строку из stdin и выводит статистику по словам, используя функции из `lib/text.py`. Печатаются общее число слов, число уникальных и топ-5. Константа `mode` задаёт формат: при `False` выводятся строки `слово:частота`, при `True` таблица `слово | частота` с шириной колонки по самому длинному слову. Запуск из папки `src`: `python -m lab03.text_stats`.

<img width="488" height="623" alt="Снимок экрана 2026-10-21 112754" src="https://github.com/user-attachments/assets/c95a554d-2eb0-469e-bbbf-f9e01ca204d5" />

# mode -> True
<img width="204" height="146" alt="Снимок экрана 2026-10-21 111641" src="https://github.com/user-attachments/assets/10502962-d94a-421c-855f-6a29328017ac" />

# mode -> False
<img width="343" height="141" alt="Снимок экрана 2026-10-21 112743" src="https://github.com/user-attachments/assets/bb1dffd9-0996-4fd9-b8a0-c780ca757065" />
