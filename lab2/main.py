from random import choice
from string import ascii_uppercase

from gost3410131 import STB
from text_helpers import str2bin, bin2str


def main():
    stb = STB()
    with open('text.txt', 'r') as f:
        text = f.read()

    KEY = ''.join(choice(ascii_uppercase) for _ in range(32))

    enc = stb.encrypt(str2bin(text), str2bin(KEY))
    enc_str = bin2str(enc)
    with open('encrypted-text.txt', 'w') as f:
        f.write(enc_str)
    print(f'Файл зашифрован')

    dec = stb.decrypt(enc, str2bin(KEY))
    dec_str = bin2str(dec)
    with open('decrypted-encrypted-text.txt', 'w') as f:
        f.write(dec_str)
    print(f'Файл расшифрован')


if __name__ == '__main__':
    main()
