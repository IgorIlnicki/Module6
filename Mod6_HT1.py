from collections import UserDict
import json
import re
import os
class Field(UserDict):
    def __init__(self):
        self.data = {}

    def checit_json(self, filename):
        if os.path.getsize("A1.json") > 0:
            print(f" Файл пустий")
        # with open(filename, 'r') as file:
        #     self.data = file.read().strip()
        #     if not self.data: # якщо файл пустий
        #         print(f" Файл пустий")
        #         kk = False
        else: 
            self.data = json.loads(self.data)
            kk = True
            return kk
        
    def save_to_json(self, filename, new_data=None, args = None):
        with open(filename, 'r') as file:
            existing_data = file.read().strip()
            if not existing_data: # якщо файл пустий
                print(f" Файл пустий")
                with open(filename, 'w') as file:   # записуємо сюди при першому виклику
                    json.dump(new_data, file, indent=4)
            else:
                existing_data = json.loads(existing_data) # завантажуємо файл в представленні Python
                print(f"existing_data: {existing_data}")
                print(f"args: {args[0]}")
                self.data = existing_data
                for i in self.data:
                    print(f" i: {i} args[{0}]: {args[0]}")
                    if i == args[0]:
                        print(f"   Ура")
                        self.data[i].append(args[1])
                        new_data2 = {}
                        new_data2 = {i: self.data[i]}  # записуємо у пустий словник телефони зі знайденим іменем
                        new_data = {**new_data, **new_data2} #  додаємо нові введені параметри до нового словника
                        print(f"self.data0: {self.data}")
                        print(f"new.data0: {new_data}")
                self.data = {**self.data, **new_data} #  об'єднуємо два словники
                print(f"   Ура 2")
                print(f"self.data2: {self.data}")
                with open(filename, 'w') as file:   # записуємо
                    json.dump(self.data, file, indent=4)

    def write_json(self, filename):
        with open(filename, 'w') as file:   # записуємо
                    json.dump(self.data, file, indent=4)         

    def load_from_json(self, filename):
        with open(filename, 'r') as json_file:
            self.data = json.load(json_file)

    def erase_json(self, filename):
        with open(filename, 'w') as file:
            json.dump({}, file)

def input_error(func):   # декоратор
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Додайте ім'я та телефон"
        except KeyError:
            return "Не задане ім'я"
        except IndexError:
            return "Не знайдено"
        except Exception as e:
            return f"Помилка: {e}"
    return inner


def parse_input(user_input): #ввод команди та аргументів
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args):
    cont = Field()
    cont.data[args[0]] = [args[1]]
    new_data = cont.data
    cont.save_to_json('A.json', new_data, args)


def list():
        i = 0
        cont =Field()
        if cont.checit_json('A1.json'):
            
        #     for key in cont.data:
        #         i +=1
        #         len2=0 
        #         print(f"{i:2}. {key:10} Телефон: """, end="")
        #         len1 = len(cont.data[key])
        #         for value in cont.data[key]:
        #             len2 +=1
        #             if len2 < len1:
        #                 print(f"{value}"", ", end="")
        #             else:
        #                 print(f"{value}")                   
        # else:
        #     print(f"Dictionary is empty")


def remove(args):
    cont = Field()
    cont.checit_json('A.json')
    print(f"Телефон: {args[0]} видалено з БД")
    cont.data.pop(args[0])
    cont.write_json('A.json') 


def list_name(args):
    cont = Field()
    cont.checit_json('A.json')
    len2=0
    for key in cont.data:
        if key == args[0]:
            print(f"Знайдено абонента: {key}")
            if len(cont.data[key]) > 1:
                for value in cont.data[key]:
                    len2 +=1
                    print(f"{len2:2}-й телефон: {value}")
                return
            else:
                value = cont.data[key][0]
                print(f"Телефон: {value}")
                return


def change_phone(args):
    cont = Field()
    cont.checit_json('A.json')
    len2=0
    for key in cont.data:
            if key == args[0]:
                if len(cont.data[key]) > 1:
                        print(f"Знайдено абонента: {key}")
                        for value in cont.data[key]:
                            len2 +=1
                            print(f"{len2:2}-й телефон: {value}")
                        k = input(print(f"Введіть порядковий номер телефона зі списку, який підлягає заміні:"))
                        if str(k.isdigit):
                            k = int(k)
                            print(f"   k = {k} ")
                            print(type(k))
                            if k > 0 and k <= len2:
                                k0 = 0
                                for i in cont.data[key]:
                            
                                    print(f"   i = {i} k0 = {k0}")
                                    if k0 == k-1:
                                        value_list = cont.data[key]  # Access the list associated with the key
                                        element = value_list[k0] 
                                        cont.data[key][k0] = args[1]
                                        print(f"Телефон: {i} замінено на: {cont.data[key][k0]}")
                                        cont.write_json('A.json')
                                        return
                                    else:
                                        k0 +=1
                            else:
                                print(f"Невірне значення порядкового номеру телефону!")
                        else:
                            print(f"Невірне введення порядкового номеру телефону!")
                            return 
                if len(cont.data[key])  == 1:
                        print(f"Знайдено абонента: {key}")
                        print(f"Телефон: {cont.data[key]} замінено на: {args[1]}")
                        # cont.data.update({key: [args[1]]})
                        cont.data[key] = [args[1]]
                        cont.write_json('A.json') 
                if len(cont.data[key]) < 1:
                    print(f"Абонента з ім'ям {args[0]} не знайдено.")  
                    return
                
# def change_name(args,contacts):
#     contacts[int(args[0])].setName(args[1])

def main():
    contacts = {}
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
            print(add_contact(args))
        elif command == "changephone":
            print(change_phone(args))
        # elif command == "changename":
        #     print(change_name(args))
        elif command == "remove":
            print(remove(args))
        elif command == "list":
            print(list())                  
        elif command == "listname":
            print(list_name(args))                   
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    
