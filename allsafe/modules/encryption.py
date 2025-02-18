from itertools import cycle

import hashlib


def sort_chars(*args) -> list[str]:
    """
    insert every character in the given texts into a list
    and sort the list
    """
    sorted_chars = []
    for arg in args:
        sorted_chars.extend(list(arg))
    sorted_chars.sort()
    return sorted_chars

def get_ords(chars: list) -> list[int]:
    return [ord(char) for char in chars]

def _get_larger_and_shorter_list(list1: list, list2: list) -> tuple[list]:
    if len(list1) > len(list2):
        return (list1, list2)
    return (list2, list1)

def add_ords(ords1: list[int], ords2: list[int]) -> list[int]:
    """This function will sum numbers of two ord lists, pairwise"""
    larger, shorter = _get_larger_and_shorter_list(ords1, ords2)
    shorter_cycle = cycle(shorter)
    result = []
    for i in larger:
        result.append(i + next(shorter_cycle))

    return result

def get_chars(ords: list) -> list[str]:
    return [chr(i) for i in ords]

def calculate_sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def _get_steps_based_on_length(cipher_len, passwd_len) -> int:
    return cipher_len // passwd_len

def _convert_hex_to_list_of_ints(hex_string: str, length: int) -> list[int]:
    """
    This function will take a hexadecimal number (`hex_string`) that will be used to generate
    numbers as many as specified in `length` (length of the result list) parameter.
    """
    nums = []
    cipher_len = len(hex_string)
    steps = _get_steps_based_on_length(cipher_len, length)
    for i in range(0, cipher_len, steps):
        nums.append(int(hex_string[i::2], base=16))
    # `hex_string` might not be divisible by `length`, and
    # that results in longer `nums` than the given `length`
    # this is a compatible option, for now.
    return nums[:length]

def turn_into_passwd(hex_string: str, length: int, passwd_chars: str) -> str:
    """
    Turn `hex_string` into a password with the given length and passwd_chars characters
    """
    nums = _convert_hex_to_list_of_ints(hex_string, length)
    new_string = ""
    n_chars = len(passwd_chars)
    for num in nums:
        new_string += passwd_chars[num%n_chars]
    return new_string

def generate_passwds(key: str, *args, lengths: tuple[int], passwd_chars: str) -> list[str]:
    """
    Encrypt texts with a key as following steps:
    - First, unicode of every single character in texts will be sorted
      and stored in a list object.
    - Then the key's unicodes will be stored in another list object.
    - Then unicodes of each list object will be summed pairwise and
      added to a new list.
    - Then the new list will be turned into a list of characters with
      assuming each item of a list (which should be an integer) as a
      unicode.
    - The said characters will be hashed with a specific algorithm.
    - The hashed data (which is a big hexadecimal number) will be
      replaced with other password-safe characters via a complex
      algorithm.
    - The final string is the result which will always be the same
      with the same given data.

    set password lengths:
    >>> encrypt(key, *info, lengths=(8, 16, 24))

    set password characters:
    >>> encrypt(key, *info, passwd_chars="abc123")
    """
    extra_strings = (arg.lower() for arg in args)
    char_list = sort_chars(*extra_strings)
    char_ords = get_ords(char_list)
    key_ords = get_ords(key)

    new_ords = add_ords(char_ords, key_ords)
    chars = get_chars(new_ords)
    text = "".join(chars)
    hashed_text = calculate_sha256(text)

    passwds = []
    for length in lengths:
        passwds.append(
            turn_into_passwd(hashed_text, length, passwd_chars)
        )

    return passwds
