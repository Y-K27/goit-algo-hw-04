contact_list = {}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if name not in contacts.keys():
            contacts[name] = phone
            return "Contact added."
        else:
            return "The contact is exist"        
    except:
        return "Wrong contact."

def check_contact(args, contacts):
    try:
        name = args
        if name[0] in contacts.keys():
            return f"Phone nomber: {contacts[name[0]]}"
        else:
            return f"Wrong contact Name: \"{name[0]}\""      
    except:
        return "Wrong argument."

def change_contact_number(args, contacts):
    try:
        name, phone = args
        if name in contacts.keys():
            contact_list[name] = phone
            return "Number chenging"
        else:
            return f"Contact Name: \"{name}\" - doesn't exist"      
    except:
        return "Wrong argument."
    
def all_contacts(contacts):
    try:
        list=''
        for item in contacts.keys():
                list+= f"Name: \"{item}\" Phone: {contact_list[item]}\n"
        return list       
    except:
        return "Wrong contact."
def main():
    print("Welcome to the assistant bot!")
    while True:
        global contact_list 
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contact_list))
            
        elif command == "all":
            print(all_contacts(contact_list))  
              
        elif command == "phone":
            print(check_contact(args, contact_list))
            
        elif command == "change":    
            print(change_contact_number(args, contact_list))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
