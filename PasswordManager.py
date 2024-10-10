from cryptography.fernet import Fernet
import cryptography  # This is required to catch cryptography-related exceptions

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    try:
        with open("Passwords.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                if "|" not in data:
                    print("Invalid entry found. Skipping.")
                    continue
                user, encrypted_passw = data.split("|")

                try:
                    decrypted_passw = fer.decrypt(encrypted_passw.encode()).decode()
                    print(f"User: {user}, Password: {decrypted_passw}")
                except cryptography.fernet.InvalidToken:
                    print(f"Error decrypting password for {user}: Invalid encryption token.")
    except FileNotFoundError:
        print("No passwords found. Add some first!")
    except Exception as e:
        print(f"An error occurred: {e}")


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue