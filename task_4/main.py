def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
        except ValueError:
            return "Give me name and phone please."

    return inner

@input_error
def parse_input(user_input) -> tuple:
    """
    Parses the input string into a command and arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(name, phone, contacts) -> str:
    """
    Adds a new contact to the dictionary.
    Checks if the contact already exists before adding.
    """
    if name in contacts:
        return f"Contact '{name}' already exists."
    else:
        contacts[name] = phone
        return "Contact added."

@input_error
def change_contact(name, phone, contacts) -> str:
    """
    Changes the phone number for an existing contact.
    """
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(name, contacts) -> str:
    """
    Shows the phone number for a specified contact.
    """
    if name in contacts:
        return f"{contacts[name]}"
    else:
        return "Contact not found."

@input_error
def show_all(contacts) -> str:
    """
    Shows all saved contacts.
    """
    if not contacts:
        return "No contacts saved."

    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    """
    The main function that controls the bot's operation.
    """
    contacts = {}
    print("Welcome to the assistant bot!")

    command_map = {
        "add": (add_contact, 2, "Invalid format. Use: add [name] [phone]"),
        "change": (change_contact, 2, "Invalid format. Use: change [name] [phone]"),
        "phone": (show_phone, 1, "Invalid format. Use: phone [name]"),
        "all": (show_all, 0, "Invalid format. 'all' takes no arguments."),
    }

    while True:
        user_input = input(f"Enter a command: ")
        
        if not user_input:
            continue
            
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
            
        elif command == "hello":
            print("How can I help you?")

        elif command in command_map:
            handler, expected_args, error_message = command_map[command]
            
            if len(args) != expected_args:
                print(error_message)
            else:
                print(handler(*args, contacts))
                
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
