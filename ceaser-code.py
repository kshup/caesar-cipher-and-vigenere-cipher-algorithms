
MAX_KEY_SIZE = 26
def getMode ():
  while True:
   print("Bir mesajı şifrelemek (e) mi yoksa şifresini çözmek(c) mi istiyorsunuz?")
   mode = input().lower()
   if mode in 'sifrele e sifre coz c'.split():
     return mode
   else:
    print('sifrele" veya "e" veya "sifre çoz" veya "c" girin.')
def getMessage():
 print('Mesajınızı girin:')
 return input()


def getKey():
 key=0
 while True:
  print('Anahtar numarasını girin (1-% s)'% (MAX_KEY_SIZE))
  key = int(input())
  if (key >= 1 and key <= MAX_KEY_SIZE):
    return key
def getTranslatedMessage(mode, message, key):
 if mode[0] == 'c':
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
mode = getMode()
message = getMessage()
key = getKey()
print('Çevrilmiş metniniz:')
print(getTranslatedMessage(mode, message, key))
