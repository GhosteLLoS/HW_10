from collections import UserDict

def input_errors(func):
    def inner(*args):
        try:
            return func(*args)
        except (KeyError, IndexError, ValueError):
            return "Not enough arguments."
    return inner


class Field():
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self):
        return self


class Name(Field):
    ...


class Phone(Field):
    ...


class Record:
    def __init__(self, name:Name, phone:Phone=None) -> None:
        self.name = name
        self.phones = [phone] if phone else []
    
    def add_number(self, phone:Phone):
        self.phones.append(phone)

    
class Addressbook(UserDict):
    def add_record(self, rec:Record):
        self.data[rec.name.value] = rec


contacts = Addressbook()

@input_errors
def add(*args):

    name = Name(args[0])
    phone = Phone(args[1])

    rec = Record(name, phone)
    
    contacts.add_record(rec)
    return f'contact {name} and phone_number {phone} adding successfully'

@input_errors
def change_phone_number(*args):
    name = Name(args[0])
    new_phone = Phone(args[1])
    if contacts.get(name):
        contacts[name] = new_phone
        return f"Phone number for contact {name} changed"
    return f"No contact with name {name}"

@input_errors
def print_phone_number(*args):
    name = Name(args[0])
    if contacts.get(name):
        return contacts[name]
    return f"No contact with name {name}"


def show_all(*args):
    if contacts:
        return '\n'.join([f'{name}: {phone}' for name, phone in contacts.items()])
    return "You have no contacts yet"


def hello(*args):
    return "How can I help you?"


def good_bye(*args):
    return 'Good bye!'


def no_command(*args):
    return "Unknown command, try again"
   
COMMANDS = {'hello': hello,
            'add': add,
            'good bye': good_bye,
            'exit': good_bye,
            'close': good_bye,
            'show all': show_all,
            'change': change_phone_number,
            'phone': print_phone_number
}


def command_handler(text):
    for kword, command in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, '').strip().split()
    return no_command, None


def main():
    print(hello())
    while True:
        user_input = (input(">>>")) 
        command, data = command_handler(user_input)
        print(command(*data))
        if command == good_bye:
            break
            

if __name__ == '__main__':
    main()