from transliterate import to_cyrillic, to_latin


def translator():
    print("Введите  'stop'', чтобы остановить программу.")
    result = ""
    while True:
        text = input('Введите текст >>> ')

        if text.isascii():
            print(to_cyrillic(text))
            result += (to_cyrillic(text) + ', ')
        else:
            print(to_latin(text))
            result += (to_latin(text) + ', ')

        if text.strip().lower() == 'stop':
            print('Спасибо за участие')
            break

    return result


print(translator())

