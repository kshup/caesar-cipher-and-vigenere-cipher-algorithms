import time

MAX_KEY_SIZE = 26


def getMode():
    while True:
        print("-----------     MENU      ------------")
        print("--                                  --")
        print("-- Sifreleme / Encrypt       ---> e --")
        print("-- Sifre Cozme / Decrypt     ---> d --")
        print("-- Kaba Kuvvet / Brute Force ---> b --")
        print("-- Cikis / Quit              ---> q --")
        print("--                                  --")
        print("--------------------------------------")
        mode = input("Secim :  ").lower()
        if mode in 'encrypt e decrypt d brute b quit q'.split():
            return mode[0]
        else:
            print("Yanlis secenek girdiniz. Lutfen kontrol ediniz..\n")


def getMessage():
    print('Mesajınızı girin:')
    return input()


def getKey():
    while True:
        print('Anahtar numarasını girin (1-% s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated


while True:
    mode = getMode()
    if mode[0] == 'q':
        break
    message = getMessage()
    if mode[0] == 'e':
        key = getKey()
        print(getTranslatedMessage(mode, message, key))
        time.sleep(1)
        continue
    if mode[0] == 'd':
        key = getKey()
        print(getTranslatedMessage(mode, message, key))
        time.sleep(1)
        continue
    if mode[0] == 'b':
        key = 0
        for key in range(1, MAX_KEY_SIZE + 1):
            print(key," ---> ", getTranslatedMessage('decrypt', message, key))
        time.sleep(1)
        continue
