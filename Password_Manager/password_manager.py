# pip install cryptography
from cryptography.fernet import Fernet # Fernet is a symmetric encryption algorithm that uses the same key to encrypt and decrypt data

''''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
# write_key() function is used to generate a key and write it to a file. We only need to run this function once to generate the key and then we can comment it out.

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
# load_key() helps for loading the key from the file and returning it.

key = load_key()
fer = Fernet(key) # fer object is created with the key loaded from the file.

def view_passwords():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode()) # password is decrypted and printed to the console.

def add_passwords():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") # passowrd is encrypted before writing it to the file

while True:
    mode = input(f"Would you like to add a new password or view existing passwords?(add/view), or q for quit: ")

    if mode == "q":
        break

    if mode == "add":
        add_passwords()
    elif mode == "view":
        view_passwords()
    else:
        print("Invalid mode")
        continue