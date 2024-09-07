from lab1.gost28147 import encode_file, decode_file


def main():
    encode_file('text.txt')
    decode_file('encrypted-text.txt')


if __name__ == '__main__':
    main()
