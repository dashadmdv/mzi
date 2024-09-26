import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime_number(bits):
    while True:
        num = random.getrandbits(bits)
        if num % 4 == 3 and is_prime(num):
            return num


def get_keys(bits: int) -> tuple:
    # генерим секретный ключ из двух простых чисел
    p = generate_prime_number(bits)
    q = generate_prime_number(bits)

    while p == q:
        q = generate_prime_number(bits)

    return p, q


def encrypt_text(p, n):
    p <<= 8
    # добавили подстроку, чтобы потом выбрать правильное решение
    p |= 0xFF
    # (p ^ 2) mod n
    return pow(p, 2, n)


def extended_euclidean(p, q):
    # расширенный алгоритм евклида
    if p == 0:
        return q, 0, 1
    else:
        gcd, y, x = extended_euclidean(q % p, p)
        return gcd, x - (q // p) * y, y


def decrypt_text(c, p, q, n):
    # находим такие числа a, b, что
    # a * p + b * q = 1
    ext_eucl = extended_euclidean(p, q)

    a, b = ext_eucl[1], ext_eucl[2]

    r = pow(c, (p+1) // 4, p)
    s = pow(c, (q+1) // 4, q)

    # китайская теорема об остатках
    # (находим 4 квадратных корня)
    x = int((a * p * s + b * q * r) % n)
    x1 = n - x
    y = int((a * p * s - b * q * r) % n)
    y1 = n - y

    return x, x1, y, y1


def find_correct_solution(solutions: list) -> int:
    # чекаем, есть ли в конце сообщения наш
    # маркер правильного решения
    bit_mask = (1 << 8) - 1
    for sol in solutions:
        n = sol & bit_mask
        if n == 0xFF:
            return sol

    return None
