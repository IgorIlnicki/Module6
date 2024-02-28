from collections import UserDict
import json

class Field:  # Базовий клас для полів запису
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    
# class Name(Field):  # Клас для зберігання імені контакту
#     # реалізація класу
# 		pass

class Record:  # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів
#     # Додавання телефонів, Видалення телефонів, Редагування телефонів, Пошук телефону.
#     # Реалізовано зберігання об'єкта Name в окремому атрибуті.
#     # Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
#     # Реалізовано методи для додавання - add_phone/видалення - remove_phone/редагування - edit_phone/пошуку об'єктів Phone - find_phone.  
    def __init__(self, name, phones=[]):
            self.name = name
            self.phones = phones

class Phone():  # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    # Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
    # def __init__(self,name,phones): # конструктор
    # f = Record(name=None, phones=None)
    def __init__(self, phones=[]):
            self.phones = phones
    def valid(self, phones):
        print(f" f= {phones}")
        for ff in self.phones:
            # print(f" ff= {ff}")
            if len(ff) <= 10:
                print(f" self.phone = {ff}")
                # return ff
            else:
                raise f'{phones} us a wrong format'
        
class AddressBook(UserDict):  # Клас для зберігання та управління записами
    # Додавання записів, Пошук записів за іменем, Видалення записів за іменем.
		# Реалізовано метод add_record, який додає запис до self.data
       # Реалізовано метод find, який знаходить запис за ім'ям, 
       # Реалізовано метод delete, який видаляє запис за ім'ям
        def __init__(self):
            self.data = {} # словник: сюди будемо скидати записи
        def write_json(self, filename):
            with open(filename, 'w') as file:   # записуємо
                json.dump(self.data, file, indent=4) 
        def load_from_json(self, filename):
            with open(filename, 'r') as json_file:
                self.data = json.load(json_file)
        def erase_json(self, filename):
            with open(filename, 'w') as file:
                json.dump({}, file) 

def parse_input(user_input): #ввод команди та аргументів
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    args0.clear()
    for a in args:
        print(f" a = {a}")
        if str(a).isdigit():
            args0.append(a)
            print(f" 0 args0 = {args0}")
    print(f" args0 = {args0}")
    return cmd, *args

def add_contact(args):
    p1 = Record(args[0], args0)
    Phone.valid(args0)
    print(f" name = {p1.name} phone = {p1.phones}")
    adr = AddressBook(args0) 
    adr.data.update({p1.name: p1.phones})
    print(f" adr = {adr.data}")

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print()

args0 = []
if __name__ == "__main__":
    main()