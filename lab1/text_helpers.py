def str_to_binary(s: str) -> list:
    # берем аски код каждого символа в строке и
    # переводим в двоичку (каждый символ длины 8 бит)
    symbols = [
        [format(ord(j), '08b') for j in s[i:i + 4]]
        for i in range(len(s) - 4, -4, -4)
    ]
    bin_repr = [''.join(symbol) for symbol in symbols]

    return bin_repr


def text_to_binary(text: str, decode=False) -> list:
    result = []

    if decode:
        bits = '08b'
    else:
        bits = '16b'

    for txt in text:
        for t in txt:
            result.append(format(ord(t), bits))

    if decode and len(result) > 1:
        new_result = []

        for i in range(0, len(result), 2):
            new_result.append(result[i] + result[i + 1])

        result = new_result

    return [sym.replace(' ', '0') for sym in result]


def binary_to_text(binary: str, bit_size: str) -> str:
    result_str = ''

    if bit_size is None:
        bit_size = 8

    for i in range(0, len(binary), bit_size):
        result_str += chr(int(binary[i:i + bit_size], 2))

    return result_str
