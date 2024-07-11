# Ability to create a Contacts in Address Book with first and last names, address, city, state, zip, phone number and email
#Ability to add a new Contact to Address Book


class Utility:
    @staticmethod
    def input_numeric(text : str, min : int, max : int) -> int:
        text = text.replace("_", " ").title()
        while True:
            try:
                number = int(input(f"Enter {text} ({min} - {max}): "))
                if number < min or number > max:
                    print(f"Please enter a number between {min} and {max}")
                    continue
                return number
            except ValueError:
                print("Please enter a valid number")    

    @staticmethod
    def input_string(text : str, min_length : int, max_length : int) -> str:
        text = text.replace("_", " ").title()
        while True:
            string = input(f"Enter {text} ({min_length} - {max_length} characters): ")
            if len(string) < min_length or len(string) > max_length:
                print(f"Please enter a string between {min_length} and {max_length} characters")
                continue
            return string

class AddressBook (Utility):
    PERSON_CONSTRAINTS = {
        "first_name" : {
            "min" : 2,
            "max" : 20,
            "type" : "str"
        },
        "last_name" : {
            "min" : 2,
            "max" : 20,
            "type" : "str"
        },
        "address" : {
            "min" : 2,
            "max" : 50,
            "type" : "str"
        },
        "city" : {
            "min" : 2,
            "max" : 20,
            "type" : "str"
        },
        "state" : {
            "min" : 2,
            "max" : 20,
            "type" : "str"
        },
        "zip_code" : {
            "min" : 000000,
            "max" : 999999,
            "type" : "int"
        },
        "phone" : {
            "min" : 1000000000,
            "max" : 9999999999,
            "type" : "int"
        },
        "email" : {
            "min" : 5,
            "max" : 50,
            "type" : "str"
        }
    }

    def __init__(self):
        self.contacts = []
        
    def add_contact(self):
        contact = {}
        for key, value in self.PERSON_CONSTRAINTS.items():
            if value["type"] == "str":
                contact[key] = self.input_string(key, value["min"], value["max"])
            else:
                contact[key] = self.input_numeric(key, value["min"], value["max"])
        self.contacts.append(contact)
        print("Contact added successfully")
        
    def display_contacts(self):
        for contact in self.contacts:
            print("\n")
            for key, value in contact.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            print("\n")



def main():
    address_book = AddressBook()
    while True:
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")
        choice = Utility.input_numeric("choice", 1, 3)
        if choice == 1:
            address_book.add_contact()
        elif choice == 2:
            address_book.display_contacts()
        else:
            break
    
    
if __name__ == "__main__":
    main()