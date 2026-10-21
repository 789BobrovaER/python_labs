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

# print(f'normalize({repr("ПрИвЕт\nМИр\t")}) -> {normalize("ПрИвЕт\nМИр\t")}')
# print(f'normalize({repr("ёжик, Ёлка")}) -> {normalize("ёжик, Ёлка")}')
# print(f'normalize({repr("Hello\r\nWorld")}) -> {normalize("Hello\r\nWorld")}')
# print(f'normalize({repr("  двойные   пробелы  ")}) -> {normalize("  двойные   пробелы  ")}')

def tokenize(text: str) -> list[str]:
    if not isinstance(text, str):
            raise TypeError('введена не строка')
    text=normalize(text)
    tok=re.findall(r'\w+(?:-\w+)*', text)
    return tok

# print(f'tokenize({repr("привет мир")}) -> {tokenize("привет мир")}')
# print(f'tokenize({repr("hello,world!!!")}) -> {tokenize("hello,world!!!")}')
# print(f'tokenize({repr("по-настоящему круто")}) -> {tokenize("по-настоящему круто")}')
# print(f'tokenize({repr("2025 год" )}) -> {tokenize("2025 год" )}')
# print(f'tokenize({repr("emoji 😀 не слово")}) -> {tokenize("emoji 😀 не слово")}')
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

# print(f'count_freq(["a","b","a","c","b","a"]) -> {count_freq(["a","b","a","c","b","a"])}')
# print(f'count_freq(["bb","aa","bb","aa","cc"]) -> {count_freq(["bb","aa","bb","aa","cc"])}')
     

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    if not isinstance(freq, dict):
        raise TypeError('введен не словарь')
    
    if not freq:
        raise ValueError('пустой словарь')
    

    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]

# print(f'top_n({repr({"a":3,"b":2,"c":1})}, n=2) -> {top_n({"a":3,"b":2,"c":1}, n=2)}')
# print(f'top_n({repr({"aa":2,"bb":2,"cc":1})}, n=2) -> {top_n({"aa":2,"bb":2,"cc":1}, n=2)}')




