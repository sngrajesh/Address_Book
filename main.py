# Ability to create a Contacts in Address Book with first and last names, address, city, state, zip, phone number and email
# Ability to add a new Contact to Address Book
# Ability to edit existing contact person using their name
# Ability to delete a person using person's name - Use Console to delete a person
# Ability to add multiple person to Address Book
# Refactor to add multiple Address Book to the System. Each Address Book has a unique Name
# Ability to ensure there is no Duplicate Entry of the same Person in a particular Address Book 
# Ability to search Person in a City or State across the multiple Address Book - Search Result
# Ability to view Persons by City or State - Maintain Dictionary of City and Person as well as State and Person
# Ability to get number of contact persons i.e. count by City or State
# Ability to sort the entries in the address book alphabetically by Person’s name


import copy 

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
            "max" : 20,
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
        
        for con in self.contacts:
            if con["first_name"] == contact["first_name"] and con["last_name"] == contact["last_name"]:
                print("Contact already exists")
                return

        self.contacts.append(contact)
        print("Contact added successfully")
    
    def add_contact_multiple(self):
        numer_of_contacts = Utility.input_numeric("number_of_contacts", 1, 100, False)
        for i in range(numer_of_contacts):
            print(f"Enter Contact Detail for user {i + 1}")
            self.add_contact()
    
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
    
    def delete_contact_using_name(self):
        first_name = self.input_string("first_name", 2, 20 , False)
        last_name = self.input_string("last_name", 2, 20, False)
        for contact in self.contacts:
            if contact["first_name"] == first_name and contact["last_name"] == last_name:
                self.contacts.remove(contact)
                print("Contact deleted successfully")
                return
        print("Contact not found")
        

class AddressBookSystem(Utility):
    def __init__(self):
        self.address_books = []
        
    def add_address_book(self):
        while True:
            book_name = self.input_string("book_name", 2, 20, False)
            for book in self.address_books:
                if book["book_name"] == book_name:
                    print("Address Book already exists")
                    continue
            address_book = AddressBook()
            self.address_books.append({
                "book_name" : book_name,
                "address_book" : address_book
            })
            print("Address Book added successfully")
            break
    
    def display_address_books(self):
        for book in self.address_books:
            print(book["book_name"])

    @staticmethod
    def print_address_book_in_format(address_books):   
        for book in address_books:
            print(f"\nAddress Book: {book['book_name']}")
            print('-'*169)
            print("|", end = "")
            for key, value in AddressBook.PERSON_CONSTRAINTS.items():
                print(f'{key:^20}', end = "|")
            print()
            print('-'*169)
            for contact  in book["address_book"].contacts:
                print("|", end = "")
                for value in contact.values():
                    print(f'{value:^20}', end = "|")
                print()
            print('-'*169)
            print()
    

    def display_address_books_in_format(self):
        self.print_address_book_in_format(self.address_books)



    def actions_on_address_book(self):
        book_name = self.input_string("book_name", 2, 20, False)
        for book in self.address_books:
            if book["book_name"] == book_name:
                address_book = book["address_book"]
                while True:
                    print("1. Add Contact")
                    print("2. Add Multiple Contact")
                    print("3. Display Contacts")
                    print("4. Edit Contact using Name")
                    print("5. Delete Contact using Name")
                    print("_. Exit")
                    choice = Utility.input_numeric("choice", 1, 9, False)
                    if choice == 1:
                        address_book.add_contact()
                    if choice == 2:
                        address_book.add_contact_multiple()
                    elif choice == 3:
                        address_book.display_contacts()
                    elif choice == 4:
                        address_book.edit_contact_using_name()
                    elif choice == 5:
                        address_book.delete_contact_using_name()
                    else:
                        break
                return
    
    def search_using_city(self):
        res_contact = []
        city_name = self.input_string("city", 2, 20, False)
        for book in self.address_books:
            address_book = book["address_book"]
            for contact in address_book.contacts:
                if contact["city"] == city_name:
                    res_contact.append(contact)
        print(res_contact)
    
    def categorize_by_city_and_state(self):
        city_dict = {}
        state_dict = {}
        for book in self.address_books:
            address_book = book["address_book"]
            for contact in address_book.contacts:
                # City categorization
                if contact["city"] not in city_dict:
                    city_dict[contact["city"]] = []
                city_dict[contact["city"]].append({
                    "first_name": contact["first_name"],
                    "last_name": contact["last_name"],
                    "address_book_name": book["book_name"]
                })
                
                # State categorization
                if contact["state"] not in state_dict:
                    state_dict[contact["state"]] = []
                state_dict[contact["state"]].append({
                    "first_name": contact["first_name"],
                    "last_name": contact["last_name"],
                    "address_book_name": book["book_name"]
                })
        return city_dict, state_dict

    def view_by_city_and_state(self):
        city_dict, state_dict = self.categorize_by_city_and_state()
        
        print("\n\nPersons according to city")
        for city, contacts in city_dict.items():
            print(f'\n{city}')
            print(64*"-")
            print("|{:^20}|{:^20}|{:^20}|".format("First Name", "Last Name", "Address Book"))
            print(64*"-")
            for contact in contacts:
                print("|{:^20}|{:^20}|{:^20}|".format(
                    contact["first_name"],
                    contact["last_name"],
                    contact["address_book_name"]
                ))
            print(64*"-")
        
        print("\n\nPersons according to state")
        for state, contacts in state_dict.items():
            print(f'\n{state}')
            print(64*"-")
            print("|{:^20}|{:^20}|{:^20}|".format("First Name", "Last Name", "Address Book"))
            print(64*"-")
            for contact in contacts:
                print("|{:^20}|{:^20}|{:^20}|".format(
                    contact["first_name"],
                    contact["last_name"],
                    contact["address_book_name"]
                ))
            print(64*"-")
    

    def view_number_of_contact_by_city_and_state(self):
        city_dict, state_dict = self.categorize_by_city_and_state()
        print("\n\nNumber of contacts according to city")
        for city, contacts in city_dict.items():
            print(f'{city} : {len(contacts)}')
        print("\n\nNumber of contacts according to state")
        for state, contacts in state_dict.items():
            print(f'{state} : {len(contacts)}')

    
    def sort_by_name(self):
        sorted_book = copy.deepcopy(self.address_books)
        #sorting by first_name last_name
        for book in sorted_book:
            address_book = book["address_book"]
            address_book.contacts.sort(key=lambda x: x["last_name"])
            address_book.contacts.sort(key=lambda x: x["first_name"])
        self.print_address_book_in_format(sorted_book)


def main():
    address_book_system = AddressBookSystem()
    while True:
        print("1. Add Address Book")
        print("2. Display Address Books")
        print("3. Perform Actions on Address Book")
        print("4. Search using city")
        print("5. Categorise by city and state")
        print("6. View number of contact by city and state")
        print("7. Display address book in format")
        print("8. Sort by name")
        print("_. Exit")
        choice = Utility.input_numeric("choice", 1, 9 , False)
        if choice == 1:
            address_book_system.add_address_book()
        elif choice == 2:
            address_book_system.display_address_books()
        elif choice == 3:
            address_book_system.actions_on_address_book()
        elif choice == 4:
            address_book_system.search_using_city()
        elif choice == 5:
            address_book_system.view_by_city_ans_state()
        elif choice == 6:
            address_book_system.view_number_of_contact_by_city_and_state()
        elif choice == 7:
            address_book_system.display_address_books_in_format()
        elif choice == 8:
            address_book_system.sort_by_name()
        else:
            break
    
if __name__ == "__main__":
    main()
    
