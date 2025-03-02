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
    """Return a list of Unicode code points for the given characters"""
    return [ord(char) for char in chars]

def _get_larger_and_shorter_list(list1: list, list2: list) -> tuple[list]:
    if len(list1) > len(list2):
        return (list1, list2)
    return (list2, list1)

def add_ords(ords1: list[int], ords2: list[int]) -> list[int]:
    """Sum numbers of two ord lists, pairwise"""
    larger, shorter = _get_larger_and_shorter_list(ords1, ords2)
    shorter_cycle = cycle(shorter)
    result = []
    for i in larger:
        result.append(i + next(shorter_cycle))

    return result

def get_chars(ords: list) -> list[str]:
    """Convert a list of Unicode code points into characters"""
    return [chr(i) for i in ords]

def calculate_sha256(text: str) -> str:
    """Calculate the SHA-256 hash of the given text"""
    return hashlib.sha256(text.encode()).hexdigest()

def _convert_hex_to_list_of_ints(hex_string: str, length: int) -> list[int]:
    """
    This function will take a hexadecimal number (`hex_string`) that will be used to generate
    numbers as many as specified in `length` (length of the result list) parameter.
    """
    nums = []
    hex_str_len = len(hex_string)
    steps = hex_str_len // length
    for i in range(0, hex_str_len, steps):
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
        new_string += passwd_chars[num % n_chars]
    return new_string

def generate_passwds(key: str, *args: str, lengths: tuple[int], passwd_chars: str) -> list[str]:
    """
    Generate passwords based on the provided key and strings.

    This function creates a list of passwords by encrypting the provided
    data using the specified key. The lengths of the generated passwords
    are determined by the `lengths` argument, and the characters used
    in the passwords are drawn from the `passwd_chars` string.

    Arguments:
        key (str):
            A string used as the encryption key to generate passwords.
        *args (str):
            A variable number of strings that will be combined to create
            the base for password generation.
        lengths (tuple[int]):
            A tuple of integers where each integer specifies the length
            of a corresponding password to be generated. The number of
            passwords generated will match the number of integers in this
            tuple.
        passwd_chars (str):
            A string containing the characters from which the passwords
            will be constructed.
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
