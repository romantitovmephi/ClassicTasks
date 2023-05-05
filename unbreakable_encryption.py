from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    # генерировать length случайных байтов
    tb: bytes = token_bytes(length)
    # преобразовать эти байты в битовую строку и вернуть ее
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy  # XOR
    print(original_key, dummy, encrypted)
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2  # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("Unbreakable encryption")
    result: str = decrypt(key1, key2)
    print(result)

# фраза передаваемая в encrypt("Unbreakable encryption")
# переводится в целое число original_key
# генерируется случайное число такой же длины dummy
# оба числа переводятся в двоичные и выполняется XOR по-битово
# получаем закодированное число encrypted
# раскодировать можно используя ключ dummy применимо к encrypted
# свойство XOR
