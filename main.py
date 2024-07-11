# Ability to create a Contacts in Address Book with first and last names, address, city, state, zip, phone number and email
#Ability to add a new Contact to Address Book
#Ability to edit existing contact person using their name

class Utility:
    @staticmethod
    def input_numeric(text : str, min : int, max : int, is_null_valid : bool) -> int:
        text = text.replace("_", " ").title()
        while True:
            try:
                number = int(input(f"Enter {text} ({min} - {max}): "))
                if is_null_valid and (number == None or number == ""):
                    return None
                if number < min or number > max:
                    print(f"Please enter a number between {min} and {max}")
                    continue
                return number
            except ValueError:
                print("Please enter a valid number")    

    @staticmethod
    def input_string(text : str, min_length : int, max_length : int, is_null_valid : bool) -> str:
        text = text.replace("_", " ").title()
        while True:
            string = input(f"Enter {text} ({min_length} - {max_length} characters): ")
            if is_null_valid and string == "":
                return ""
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
                contact[key] = self.input_string(key, value["min"], value["max"], False)
            else:
                contact[key] = self.input_numeric(key, value["min"], value["max"] , False)
        self.contacts.append(contact)
        print("Contact added successfully")
        
    def display_contacts(self):
        for contact in self.contacts:
            print("\n")
            for key, value in contact.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
            print("\n")
            
    def edit_contact_using_name(self):
        first_name = self.input_string("first_name", 2, 20 , False)
        last_name = self.input_string("last_name", 2, 20, False)
        print("Press Enter to skip")
        for contact in self.contacts:
            if contact["first_name"] == first_name and contact["last_name"] == last_name:
                for key, value in self.PERSON_CONSTRAINTS.items():
                    if value["type"] == "str":
                        val = self.input_string('new ' + key, value["min"], value["max"], True)
                        if val != "":
                            contact[key] = val
                    else:
                        val = self.input_numeric('new ' + key, value["min"], value["max"] , True)
                        if val != None and val != "":
                            contact[key] = val
                print("Contact updated successfully")
                return

def main():
    address_book = AddressBook()
    while True:
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Edit Contact using Name")
        print("_. Exit")
        choice = Utility.input_numeric("choice", 1, 4 , False)
        if choice == 1:
            address_book.add_contact()
        elif choice == 2:
            address_book.display_contacts()
        elif choice == 3:
            address_book.edit_contact_using_name()
        else:
            break
    
    
if __name__ == "__main__":
    main()