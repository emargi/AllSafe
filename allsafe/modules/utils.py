from string import (
    digits, ascii_letters, punctuation
)


PASSWORD_CHARACTERS = digits + ascii_letters + punctuation


def passwd_chars_filter(chars: str):
    """
    if chars is an empty string, default characters will be returned.
    if chars is not empty and does not have at least 4 unique characters,
    ValueError will be raised.
    a unique and sorted string of characters inside chars will be returned
    otherwise.
    """
    if not chars:
        return PASSWORD_CHARACTERS
    new_chars = "".join(sorted(set(chars)))
    if len(new_chars) < 4:
        raise ValueError("chars must have at least 4 unique characters")
    return new_chars

def passwd_length_filter(input_length: str):
    if not input_length.isdigit():
        raise ValueError("input_length string must only have digits")
    length = int(input_length)
    if not 3 < length < 65:
        raise ValueError("length must be between 4-64")
    return length
