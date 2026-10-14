def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold==True : text= text.casefold()
    else: text= text.lower()

    if yo2e==True: text=text.replace('ё','е').replace('Ё','Е')
    text=text.strip()
    text=' '.join(text.split())
    return text
print(normalize("ПрИвЕт\nМИр\t"))