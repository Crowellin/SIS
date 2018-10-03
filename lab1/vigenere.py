dic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def vigenere_cypher(file, mode):
    with open(file) as f:
        message = f.readlines()
        key = 'DASHKOVA'
        # input('Word Key: ')
        text = ''
        if mode == 'encrypt':
            text = translate(key, message, 'encrypt')
        elif mode == 'decrypt':
            text = translate(key, message, 'encrypt')
        file = open('encrypted/encrypt.txt', 'w')
        file.write(text)
        file.close()
        print('Done. ')
    return text


def translate(key, message, mode):
    translated = ''  # stores the encrypted/decrypted message string
    index = 0
    key = key.upper()
    for symbol in message:
        # loop through each character in message
        num = dic.find(symbol.upper())
        if num != -1 or symbol == ' ':
            # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += dic.find(key[index])
                # add if encrypting
            elif mode == 'decrypt':
                num -= dic.find(key[index])
                # subtract if decrypting

            num %= len(dic)
            # handle the potential wrap-around

            # add the encrypted/decrypted symbol to the end of translated.
            if symbol.isupper():
                translated += dic[num]
            elif symbol.islower():
                translated += dic[num].lower()

            index += 1  # move to the next letter in the key
            if index == len(key):
                index = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated += symbol
    return translated
