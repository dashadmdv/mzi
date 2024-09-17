
def str2bin(st):
    return [int(i) for i in ''.join('{0:08b}'.format(ord(x), 'b') for x in st)]


def bin2str(input_list):
    res = ''

    if len(input_list) % 8:
        padding = [0 for _ in range(8 - len(input_list) % 8)]
        input_list = padding + input_list
    for i in range(0, len(input_list), 8):
        x = 0
        for j in range(i, i + 8):
            x = x * 2 + input_list[j]
        res += chr(x)
    return res

