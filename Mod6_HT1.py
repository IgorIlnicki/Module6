from collections import UserDict
import json
class Contact(UserDict):
    def __init__(self):
        self.data = {}

    def getName(self):
        return self.name


    def get_list(self, name):
        # Retrieve a value from the dictionary based on the key

        return self.data.get(name)




    
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
                    print(f" i: {i}")
                    if i == args[0]:
                        print(f"   Ура")
                        self.data[i].append(args[1])
                        print(f"self.data: {self.data}")
                    else:
                        self.data = {**self.data, **new_data} #  об'єднуємо два словники
                        print(f"   Ура 2")
                # existing_data.update(new_data) # додаємо до них новий запис
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
    return cmd, *args

def add_contact(args):
    cont = Contact()
    cont.data[args[0]] = [args[1]]
    new_data = cont.data
    cont.save_to_json('A.json', new_data, args)

  
def list():
        i = 0
    # with open('A.json', 'r') as file:
    #     json_data = json.load(file)
        cont = Contact()
        # new_obj.data.update(json.loads(json_data))
        print(f" 2   {cont.data}")
        for key in cont.data:
            i +=1
            print(f"{i:2}. {key:10} Телефон: {cont.data[key]}")



def change_phone(args):
    # contacts[int(args[0])].setPhone(args[1])
    # return f"Phone for record {args[0]} changed to {args[1]}"
    cont = Contact()
    cont.load_from_json('A.json')
    for key in cont.data:
        if key == args[0]:
           cont.data[key] = args[1]
    cont.erase_json('A.json')
    cont.save_to_json('A.json', new_data=cont.data)


def change_name(args,contacts):
    contacts[int(args[0])].setName(args[1])

def print_phones(args,contacts):
    for key in contacts:
        contacts[key].print()

def changeColWidth(args,contacts):
    for contact in contacts.values():
        contact.setColWidth([int(i) for i in args])
    
def writeToCSV(args,contacts):
    with open(args[0],"w+") as csvfile:
        for key in contacts:
            csvfile.write(contacts[key].getContactAsCSV())

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
        elif command == "changename":
            print(change_name(args))
        elif command == "width":
            print(changeColWidth(args, contacts))
        elif command == "print":
            print(print_phones(args, contacts))
        elif command == "list":
            print(list())                  
        elif command == "tocsv":
            print(writeToCSV(args,contacts))                   
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    
