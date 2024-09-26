def text_to_int(text: str) -> int:
    res = 0

    for i in range(len(text)):
        res = (res + ord(text[i])) << 16

    return res


def file_to_int(input_text: str):
    text = [
        [
            text[i:i + 32] for i in range(0, len(text), 32)
        ]
        for text in input_text]

    i_text = [
        [text_to_int(t_iter) for t_iter in t]
        for t in text]

    return i_text


def int_to_text(value: int) -> str:
    res = []
    while value != 0:
        res.append(chr((value) & 0xFFFF))
        value >>= 16

    res = res[1:]
    return ''.join(res[::-1])


def int_to_file(results):
    output_res = []
    for res in results:
        if res is not None:
            output_res.append(
                int_to_text(res >> 8))
    return output_res
