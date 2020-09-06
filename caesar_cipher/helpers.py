def cipher(body: str, count: int):
    text = ""
    for character in body:
        if ord(character) > 64 and ord(character) < 91:
            character = chr(ord(character) + count)
            if ord(character) > 90:
                character = chr(ord(character) - 26)
            if ord(character) < 65:
                character = chr(ord(character) + 26)

        if ord(character) > 96 and ord(character) < 123:
            character = chr(ord(character) + count)
            if ord(character) > 122:
                character = chr(ord(character) - 26)
            if ord(character) < 97:
                character = chr(ord(character) + 26)

        text = text + character
    return text


def decipher(body, count):
    return cipher(body, -count)
