from collections import UserDict
from functools import reduce
import json
import datetime
class BaseClass:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    
class Phone(BaseClass):
    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            print(f'Формат телефону: {phone} задано невірно.')
            raise main()
        
class Name(BaseClass):
    pass
class Birthday(BaseClass):
    def __init__(self, dayb):
        print(f"day = {dayb}")
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
            spec_data = datetime.datetime(year=int(dayb[1]), month=int(dayb[2]), day=int(dayb[3]))
            dayb = spec_data
            print(f"spec_date = {dayb}")
        except ValueError:
            print(f"Неправильне введення дати. Використовуйте шаблон: YYYY.MM.DD")
            raise main()

class Record: 
    def __init__(self, name):
        self.name = name
        self.phones = None
        self.birthday = None

    def add_date(self, args):
        self.birthday = args
        print(f"self.birthday = {self.birthday}")
        Birthday(self.birthday)

    def add_phone(self, phon):
        self.phones = phon
        Phone(self.phones)

class AddressBook(UserDict):  # Клас для зберігання та управління записами
    def __init__(self):
        self.data1 = {}
    def add_record(self, name, phones):
        self.checit_json(r'D:\Projects\Module6\Module6\A1.json')
        kk = False
        for key in self.data1:
            if key == name:
                self.data1[key].append(phones)
                kk = True
        if kk !=True:
            phones = [phones]
            self.data1.update({name: phones})
        self.write_json(r'D:\Projects\Module6\Module6\A1.json')
        print (f'Контакт користувача додано.')

    def add_birthday(self, name, birthday):
        self.checit_json(r'D:\Projects\Module6\Module6\A1.json')
        if self.data1[name]:
                self.data1.update({"birthday":birthday})
                self.write_json(r'D:\Projects\Module6\Module6\A1.json')
                print (f'День народження користувача додано.')
        else:
            print(f"Користувача {name} не знайдено: помилка вводу імені") 

    # def add_contact(args, book: AddressBook):
    #     name, phone, *_ = args
    #     record = book.find(name)
    #     message = "Contact updated."
    #     if record is None:
    #         record = Record(name)
    #         book.add_record(record)
    #         message = "Contact added."
    #     if phone:
    #         record.add_phone(phone)
    #     return message

    def list(self):
        self.checit_json(r'D:\Projects\Module6\Module6\A1.json')
        i = 0
        for key in self.data1:
                i +=1
                len2=0 
                print(f"{i:2}. {key:10} Телефон: """, end="")
                len1 = len(self.data1[key])
                for value in self.data1[key]:
                    len2 +=1
                    if len2 < len1:
                        print(f"{value}"", ", end="")
                    else:
                        print(f"{value}")   

    def find_name(self, name):
        self.checit_json(r'D:\Projects\Module6\Module6\A1.json')
        kk = False
        i = 0
        for key in self.data1:
            if key == name:
                len1 = len(self.data1[key])
                if len1 > 1:
                    print(f"{len1} телефони користувача {name} знайдено:")  
                else:
                     print(f"Телефон користувача {name} знайдено:")  
                for value in self.data1[key]:
                    i +=1
                    print(f"{i:5}.  {value}")   
                kk = True
        if kk !=True:
            print(f"Телефон користувача {name} не знайдено.")   

    def remove_name(self, name):
        self.checit_json(r'D:\Projects\Module6\Module6\A1.json')
        try:
            self.data1.pop(name)
            print(f"Інформація про користувача {name} видалена") 
            self.erase_json(r'D:\Projects\Module6\Module6\A1.json')
            self.write_json(r'D:\Projects\Module6\Module6\A1.json')
        except Exception as error:
            print(f"Користувача {name} не знайдено: помилка вводу {error}")  

    def change_name(self, name, name2):
        self.checit_json(r'D:\Projects\Module6\Module6\A1.json')
        if self.data1.get(name) != None:
            # print(f" name = {name} name2 = {name2} a = {self.data1.get(name)}")
            self.data1[name2] = self.data1.pop(name)
            self.erase_json(r'D:\Projects\Module6\Module6\A1.json')
            self.write_json(r'D:\Projects\Module6\Module6\A1.json')
            print(f"Ім'я користувача {name} змінено на {name2}") 
        else: 
            print(f"Користувача {name} не знайдено: помилка вводу імені") 

    def change_phone(self, name, phon):
        i = 0
        self.checit_json(r'D:\Projects\Module6\Module6\A1.json')
        if self.data1.get(name) != None:
            for value in self.data1[name]:
                i +=1
                print(f"{i:5}.  {value}")   
            if i > 1:
                number_tel = input("Який телефон змінюємо: введіть його порядковий номер:")
                if number_tel.isdigit():
                    number_tel = int(number_tel)
                    if number_tel > 0 and number_tel <= len(self.data1[name]): 
                        self.data1[name][number_tel - 1] = phon
                        print(f" self.data1[name][number_tel - 1] = {self.data1[name][number_tel - 1]}  phon = {phon}")
                    else:
                        print(f"Невірний порядковий номер {number_tel}")
                        raise main()
                else:
                    print(f"Невірний порядковий номер {number_tel}")
                    raise main()
            else:
                 self.data1[name] = [phon]
            self.erase_json(r'D:\Projects\Module6\Module6\A1.json')
            self.write_json(r'D:\Projects\Module6\Module6\A1.json')
            print(f"Телефон користувача {name} змінено на {phon}")
            i = 0
            for value in self.data1[name]:
                i +=1
                print(f"{i:5}.  {value}") 
        else: 
            print(f"Користувача {name} не знайдено: помилка вводу імені")
            raise main()

    def write_json(self, filename):
        with open(filename, 'w') as file:   # записуємо
            json.dump(self.data1, file, indent=4)

    def checit_json(self, filename):
        with open(filename, 'r+') as file:
            file_data = file.read().strip()
            if not file_data: # якщо файл пустий
                # print(f" Файл пустий")
                kk = False
            else:
                self.data1 = json.loads(file_data)
                # print (f'   data1 = {self.data1}')
                kk = True
            return kk
    def erase_json(self, filename):
        with open(filename, 'w') as file:
            json.dump({}, file)

def parse_input(user_input): #ввод команди та аргументів
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    # args0.clear()
    # for a in args:
    #     print(f" a = {a}")
    #     if str(a).isdigit():
    #         args0.append(a)
    #         print(f" 0 args0 = {args0}")
    # print(f" args0 = {args0}")
    return cmd, *args

def main():
        addressBook = AddressBook()

        print("Ласкаво просимо до бота-помічника!")
        while True:
            user_input = input("Введіть команду: ")
            command, *args = parse_input(user_input)
            print(f"000 comand = {command} args = {args}")
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                record = Record(args[0])
                record.add_phone(args[1])
                addressBook.add_record(record.name, record.phones)
            elif command == "list":
                addressBook.list() 
            elif command == "findname":
                addressBook.find_name(args[0])
            elif command == "remove":
                addressBook.remove_name(args[0])
            elif command == "changename":
                addressBook.change_name(args[0],args[1])
            elif command == "changephone":
                record = Record(args[0])
                record.add_phone(args[1])
                addressBook.change_phone(record.name, record.phones)
            elif command == "addbirthday":
                print(f"   Ми тут")
                record = Record(args[0])
                record.add_date(args)  # birthday
                addressBook.add_birthday(record.name, record.birthday)
            else:
                print("Invalid command.")


if __name__ == "__main__":
    main()