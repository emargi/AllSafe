from string import (
    digits, ascii_letters, punctuation
)
from math import log2
from typing import Union


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

def passwd_length_filter(length: Union[str, int]):
    if isinstance(length, str):
        if not length.isdigit():
            raise ValueError("length should contain only digits")
        length = int(length)

    if not 3 < length < 65:
        raise ValueError("length must be between 4-64")
    return length

def get_passwd_score(passwd: str, passwd_len: int):
    # classic password score system
    score = 0

    # character variety
    if any(c.islower() for c in passwd):
        score += 1
    if any(c.isupper() for c in passwd):
        score += 1
    if any(c.isdigit() for c in passwd):
        score += 1
    if any(c in punctuation for c in passwd):
        score += 1

    # length
    score += (passwd_len-8) // 2

    return score

def get_meaningful_emoji(passwd_score: int):
    if passwd_score < 4:
        return "🔓"
    if passwd_score < 8:
        return "🔒"
    if passwd_score < 12:
        return "🔏"
    return "🔐"
