from string import (
    digits, ascii_letters, punctuation
)


PASSWORD_CHARACTERS = digits + ascii_letters + punctuation
PASSWORD_LENGTHS = (8, 16, 24)


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

def passwd_length_filter(length: str | int):
    if isinstance(length, str):
        if not length.isdigit():
            raise ValueError("length should contain only digits")
        length = int(length)

    if not 3 < length < 65:
        raise ValueError("length must be between 4-64")
    return length

def get_meaningful_emoji(passwd: str, passwd_len: int):
    # this is simple and temporary
    # TODO: update this function
    if passwd_len < 8:
        return "🔓"
    if passwd_len > 21:
        return "🔐"

    used_chars = set(passwd)
    chars_count = len(used_chars)

    if chars_count < passwd_len:
        return "🔒"
    # short yet strong password
    return "🔏"
