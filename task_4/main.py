from typing import Dict, List, Tuple

ContactsBook = Dict[str, str]
ParsedCommand = Tuple[str, List[str]]


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
        except ValueError:
            return "Invalid format. Use: [command] [name] [phone]."

    return inner


@input_error
def parse_input(user_input: str) -> ParsedCommand:
    """
    Parse raw user input into a command and argument list.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, args


@input_error
def add_contact(args: List[str], contacts: ContactsBook) -> str:
    """
    Add a new contact to the dictionary.
    """

    name, phone = args

    if name in contacts:
        return f"Contact '{name}' already exists."

    contacts[name] = phone

    return "Contact added."


@input_error
def change_contact(args: List[str], contacts: ContactsBook) -> str:
    """
    Change the phone number for an existing contact.
    """
    name, phone = args

    if name not in contacts:
        raise KeyError

    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: List[str], contacts: ContactsBook) -> str:
    """
    Show the phone number for a specified contact.
    """
    return contacts[args[0]]


@input_error
def show_all(_: List[str], contacts: ContactsBook) -> str:
    """
    Show all saved contacts.
    """
    if not contacts:
        return "No contacts saved."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


@input_error
def greet(*args) -> str:
    """
    Respond to the hello command.
    """
    return "How can I help you?"


COMMANDS = {
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": show_all,
    "hello": greet,
}


CLOSE_COMMANDS = ["close", "exit"]


def main():
    """
    The main function that controls the bot's operation.
    """
    contacts: ContactsBook = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in CLOSE_COMMANDS:
            print("Good bye!")
            break

        handler = COMMANDS.get(command)

        if handler is None:
            print("Invalid command.")
            continue

        result = handler(args, contacts)

        if result:
            print(result)


if __name__ == "__main__":
    main()
