from string import (
    digits, ascii_letters, punctuation
)
from typing import Union


PASSWORD_CHARACTERS = digits + ascii_letters + punctuation
PASSWORD_LENGTHS = (8, 16, 24)


def passwd_chars_filter(chars: str):
    """
    Validates the provided string as password characters or returns
    the default string of characters

    if `chars` is empty, the default string of characters will be
    returned. if the length of `chars` is less than 4, ValueError
    will be raised. Otherwise, a unique and sorted string of
    characters from `chars` will be returned.
    """
    if not chars:
        return PASSWORD_CHARACTERS
    new_chars = "".join(sorted(set(chars)))
    if len(new_chars) < 4:
        raise ValueError("chars must have at least 4 unique characters")
    return new_chars

def passwd_length_filter(length: Union[str, int]):
    """Validates the provided password length"""
    if isinstance(length, str):
        if not length.isdigit():
            raise ValueError("length should contain only digits")
        length = int(length)

    if not 3 < length < 65:
        raise ValueError("length must be between 4-64")
    return length

def get_passwd_score(passwd: str, passwd_len: int):
    """
    Calculates a score for the given password based on its
    character variety and length.
    """
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

    # for every 2 characters over 8, +1 point is added
    # for every 2 characters fewer than 8, -1 point is
    # subtracted
    score += (passwd_len-8) // 2

    return score

def get_meaningful_emoji(passwd_score: int):
    """
    Returns a meaningful emoji based on the password score.

    The emoji reflects the strength of the password, with different 
    emojis representing different score ranges.
    """
    if passwd_score < 4:
        return "🔓"
    if passwd_score < 8:
        return "🔒"
    if passwd_score < 12:
        return "🔏"
    return "🔐"
