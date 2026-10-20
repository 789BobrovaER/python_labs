import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    
    if not isinstance(text, str):
        raise TypeError('введена не строка')
    
    if casefold:
        text = text.casefold()
    else: 
        text = text.lower()
    if yo2e:
        text = text.replace('ё', 'е')
    text = text.strip()
    text = ' '.join(text.split())
    if not text:
        raise ValueError('строка пуста')
    return text

print(f'normalize({repr("ПрИвЕт\nМИр\t")}) -> {normalize("ПрИвЕт\nМИр\t")}')
print(f'normalize({repr("ёжик, Ёлка")}) -> {normalize("ёжик, Ёлка")}')
print(f'normalize({repr("Hello\r\nWorld")}) -> {normalize("Hello\r\nWorld")}')
print(f'normalize({repr("  двойные   пробелы  ")}) -> {normalize("  двойные   пробелы  ")}')

def tokenize(text: str) -> list[str]:
    if not isinstance(text, str):
            raise TypeError('введена не строка')
    text=normalize(text)
    tok=re.findall(r'\w+(?:-\w+)*', text)
    return tok
print(tokenize("ПрИвЕт\nМИр\t"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    if not isinstance(tokens, list):
        raise TypeError('Введен не список')

    if not all(isinstance(token, str) for token in tokens):
        raise TypeError('все токены должны быть строками')
    
    number = {}

    for token in tokens:
        if token in number:
            number[token] += 1
        else:
            number[token] = 1
    return number

print(count_freq(["a","b","a","c","b","a"]))        

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    if not isinstance(freq, dict):
        raise TypeError('введен не словарь')
    
    if not freq:
        raise ValueError('пустой словарь')
    

    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]





