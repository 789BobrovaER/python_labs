from lib.text  import normalize, tokenize, count_freq, top_n

mode = False


def main():
    text = input()

    text = normalize(text)
    tokens = tokenize(text)
    freq = count_freq(tokens)
    top_words = top_n(freq)

    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(freq.items())}')
    print('Топ-5:')

    if mode:
        if top_words:
            r = max(len(word) for word, count in top_words)

            print(f'{'слово':<{r}} | частота')
            print('-' * (r + 10))

            for word, count in top_words:
                print(f'{word:<{r}} | {count}')

    else:
        for word, count in top_words:
            print(f'{word}:{count}')



if __name__ == "__main__":
    main()

