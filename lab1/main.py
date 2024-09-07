from lab1.gost28147 import encode_file, decode_file


def main():
    encode_file('text.txt')
    encode_file('encrypted-text.txt', decode=True)


if __name__ == '__main__':
    main()
