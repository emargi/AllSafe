from allsafe.modules import ConsoleStream, generate_passwd, utils


__version__ = "1.4.5"

def handle_inputs(console: ConsoleStream):
    addr_sample = console.styles.gray("(e.g Battle.net)")
    addr = console.ask(f"Enter app address/name {addr_sample}")

    username_sample = console.styles.gray("(e.g user123)")
    username = console.ask(f"Enter username {username_sample}")

    case_note = console.styles.gray("(case-sensitive)")
    note = "(do [bold]NOT[/bold] forget this), " + case_note
    secret_key = console.ask(f"Enter secret key {note}")

    return (secret_key, addr, username)

def print_passwds(console: ConsoleStream, passwds: list):
    md_passwds = [console.styles.passwd(i) for i in passwds]
    console.write(
        "\n"
        f"🔒 8-Length Password:\t{md_passwds[0]}\n"
        f"🔏 16-Length Password:\t{md_passwds[1]}\n"
        f"🔐 24-Length Password:\t{md_passwds[2]}\n"
    )

def generate_custom_password(console: ConsoleStream, *args):
    length_note = console.styles.gray("(between 4-64)")
    length = console.ask(f"Enter the length {length_note}",
                         func=utils.passwd_length_filter)

    chars_note = console.styles.gray("(enter for default)")
    chars = console.ask(f"Enter password characters {chars_note}",
                        func=utils.passwd_chars_filter)

    passwd_list = generate_passwd(*args, lengths=(length,), passwd_chars=chars)
    passwd = passwd_list[0]
    console.write(f"\n✅ Here you go: {console.styles.passwd(passwd)}")

def main():
    console = ConsoleStream()
    description = (
        "Get unique password for every app. No need to remeber all of them.\n"
        "No data stored and no internet needed. Use it before every sign-in."
    )
    console.panel("[bold]AllSafe[/bold] Modern Password Generator",
                  description, style=console.styles.GRAY)
    console.write(":link: Github: https://github.com/emargi/allsafe")
    console.write(":gear: Version: " + __version__ + "\n")

    inputs = handle_inputs(console)
    # default keyword arguments
    kwargs = {
        "lengths": (8, 16, 24),
        "passwd_chars": utils.PASSWORD_CHARACTERS,
    }
    passwds = generate_passwd(*inputs, **kwargs)
    print_passwds(console, passwds)

    want_custom_passwd = console.ask(
        "Do you want custom length password?",
        choices=['y', 'n'],
        default='n',
        show_default=False,
        case_sensitive=False,
    )
    if want_custom_passwd == 'n':
        return
    generate_custom_password(console, *inputs)


def run():
    try:
        main()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run()
