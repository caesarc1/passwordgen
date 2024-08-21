saved_passwords = {"Facebook": 123}

def show_passwords():
    if not saved_passwords:
        print("You don't have any saved passwords.")
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


def create_password():
    decision = input("Do you want to create a new password?\nPress 1 to YES or 2 to NO\n")

    if decision not in ["1", "2"]:
        print("Invalid option")
        return
    
    if decision == "2":
        print("Ok!")
    else:
        new_name = input("How do you want to call your new password?\n")
        new_pass = input("Ok! Now type the password.\n")

        checking = input(f"The password is correct?\nPassword: {new_pass}\nPress 1 to YES or 2 to NO\n")

        while checking == "2":
            new_pass = input("Ok! Now type the correct password.\n")
            checking = input(f"The password is correct?\nPassword: {new_pass}\nPress 1 to YES or 2 to NO\n")
        
        saved_passwords[new_name] = new_pass
        print("Password saved!")

show_passwords()

create_password()

show_passwords()
