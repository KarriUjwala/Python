import re

def validate_password(password, username, last_three_passwords):

    if len(password) < 10:
        return False, 

    if not (any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in '@#$%&*!' for c in password)):
        return False, 

    if re.search(r'(.)\1\1\1', password):
        return False, 

    if username:
        for i in range(len(username) - 2):
            if username[i:i+3] in password:
                return False, 

    for old_password in last_three_passwords:
        if password == old_password:
            return False, 

    return True, 


def main():
    username = input("Enter username (leave blank if not applicable): ")
    last_three_passwords = []

    for i in range(3):
        last_three_passwords.append(input(f"Enter the last password {i+1}: "))

    while True:
        password = input("Enter a new password: ")
        is_valid, message = validate_password(password, username, last_three_passwords)
        if is_valid:
            print("Password successfully set!")
            break
        else:
            print("Invalid password:", message)


if __name__ == "__main__":
    main()
