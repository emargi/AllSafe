from allsafe.modules import encrypt
from allsafe.modules.encryption import PASSWORD_CHARACTERS


def test_passwdord_generator():
    test_key = "test"
    test_app = "Battle.net"
    test_username = "unknown999"

    passwds = encrypt(test_key, test_app, test_username)
    for passwd in passwds:
        assert isinstance(passwd, str)
        for char in passwd:
            assert char in PASSWORD_CHARACTERS

