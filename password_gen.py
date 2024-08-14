import random

saved_passwords = {"Facebook": 123}

def show_passwords():
    if not saved_passwords:
        print("You don't have any saved passwords.")

        return 0
    else:
        print("Hi! These are your saved passwords:\n")

        for password in saved_passwords:
            print(password)
    
        chosen_pass = input("\nWhich password do you want to show?\n")
        password = saved_passwords.get(chosen_pass)
        
        if password:
            print(f"\nName: {chosen_pass}\nPassword: {password}\n")
        else:
            print("Password name not found.")

create = show_passwords()

def create_password():
    if create == 0:
        decision = input("Do you want to create a password?\nPress 1 to YES or 2 to NO\n")
    else:
        decision = input("Do you want to create another password?")

    if decision != 1 or 2:
        print("Invalid option")
    else:
        print("Ok")

create_password()

