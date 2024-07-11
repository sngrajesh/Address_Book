# Ability to create a Contacts in Address Book with first and last names, address, city, state, zip, phone number and email

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

def input_string(text : str, min_length : int, max_length : int) -> str:
    text = text.replace("_", " ").title()
    while True:
        string = input(f"Enter {text} ({min_length} - {max_length} characters): ")
        if len(string) < min_length or len(string) > max_length:
            print(f"Please enter a string between {min_length} and {max_length} characters")
            continue
        return string
                          
person = {
    "first_name" : "",
    "last_name" : "",
    "address" : "",
    "city" : "",
    "state" : "",
    "zip_code" : None,
    "phone" : None,
    "email" : ""
}

person_constraints = {
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


for key in person:
    if person_constraints[key]["type"] == "int":
        person[key] = input_numeric(key, person_constraints[key]["min"], person_constraints[key]["max"])
    else:
        person[key] = input_string(key, person_constraints[key]["min"], person_constraints[key]["max"])
        
        
print(person)