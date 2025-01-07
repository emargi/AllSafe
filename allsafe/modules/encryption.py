import hashlib
from string import ascii_letters, punctuation, digits


PASSWORD_CHARACTERS = digits + ascii_letters + punctuation

def sort_chars(*args) -> list[str]:
    sorted_chars = []
    for arg in args:
        sorted_chars.extend([i for i in arg])
    sorted_chars.sort()
    return sorted_chars

def get_ords(chars: list) -> list[int]:
    return [ord(char) for char in chars]


def add_ords(ords1: list, ords2: list) -> list[int]:
    n_ords1, n_ords2 = len(ords1), len(ords2)
    result_ords = []
    for i in range(max(n_ords1, n_ords2)):
        result_ords.append(
            ords1[i%n_ords1] +
            ords2[i%n_ords2]
        )

    return result_ords

def get_chars(ords: list) -> list[str]:
    return [chr(i) for i in ords]

def calculate_sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def _get_steps_based_on_length(cipher_len, passwd_len) -> int:
    return cipher_len // passwd_len

def _convert_hex_to_list_of_ints(hex_string: str, length: int) -> list[int]:
    nums = []
    cipher_len = len(hex_string)
    steps = _get_steps_based_on_length(cipher_len, length)
    for i in range(0, cipher_len, steps):
        nums.append(int(hex_string[i::2], base=16))
    return nums

def turn_into_passwd(hex_string: str, length: int) -> str:
    nums = _convert_hex_to_list_of_ints(hex_string, length)
    new_string = ""
    n_chars = len(PASSWORD_CHARACTERS)
    for num in nums:
        new_string += PASSWORD_CHARACTERS[num%n_chars]
    
    return new_string

def encrypt(key, *args):
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
      replaced with a other password-safe characters via a complex
      algorithm.
    - The final string is the result which will always be the same
      with the same given data.
    
    Default Lengths are 8, 16, 24
    """
    char_list = sort_chars(*args)
    char_ords = get_ords(char_list)
    key_ords = get_ords(key)

    new_ords = add_ords(char_ords, key_ords)
    chars = get_chars(new_ords)
    text = "".join(chars)
    hashed_text = calculate_sha256(text)
    passwds = []
    for num in (8, 16, 24):
        passwds.append(turn_into_passwd(hashed_text, num))
    
    return passwds
