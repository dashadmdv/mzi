import rabin as rb
from lab3.text_helpers import file_to_int, int_to_file


def read_file(filename: str):
    try:
        with open(filename, 'r') as file:
            result = file.read()
            file.close()
        return result
    except Exception:
        print("Неверный формат файла")


def read_file_lines(filename: str):
    try:
        with open(filename, 'r') as file:
            result = file.readlines()
            file.close()
        return result
    except Exception:
        print("Неверный формат файла")


def write_file(filename: str, value):
    try:
        with open(filename, 'w') as file:
            if type(value) is list:
                if type(value[0]) is list:
                    for v in value:
                        file.writelines(v)
            else:
                file.writelines(value)

            file.close()
    except Exception:
        print("Неверный формат файла")


def get_max(text: list) -> int:
    max_len = 0

    for temp in text:
        for t in temp:
            value = t.bit_length()
            if max_len < value:
                max_len = value

    return max_len


def rabin_processing(input: str):
    # переводим файл в численный вид
    input_text = read_file(f'{input}.txt')

    i_text = file_to_int(input_text)

    max_bit_len = get_max(i_text)

    # получаем рандомные простые числа
    p, q = rb.get_keys(max_bit_len)
    # получаем с секретный ключ
    n = p * q

    # шифруем
    enc_int = [
        [
            f'{rb.encrypt_text(it, n)}\n' for it in temp
        ]
        for temp in i_text]

    output = f'encrypted-{input}.txt'
    write_file(output, enc_int)

    # расшифровываем зашифрованный ранее файл
    enc_int = read_file_lines(output)
    enc_int = [int(elem) for elem in enc_int]

    # получаем 4 решения
    solutions = [rb.decrypt_text(enc, p, q, n) for enc in enc_int]
    # выбираем из 4 решений правильное
    results = [rb.find_correct_solution(sol) for sol in solutions]

    output_res = int_to_file(results)

    write_file(f'decrypted-{output}', ''.join(output_res))


def main():
    rabin_processing('text')


if __name__ == '__main__':
    main()
