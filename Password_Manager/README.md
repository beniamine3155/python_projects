# Password Manager

A **Password Manager** built with Python, using the **cryptography** library to securely encrypt and decrypt passwords. This tool helps you manage your account credentials efficiently and securely.

## 📋 Overview

This password manager allows you to:

- Add new account credentials with encryption.
- View existing credentials by decrypting the stored passwords.
- All passwords are securely encrypted using the **Fernet symmetric encryption algorithm**.

## 🛠 Features

- **Encryption**: Passwords are encrypted before being saved to a file.
- **Decryption**: Encrypted passwords are decrypted and displayed only when needed.
- **File-based storage**: Credentials are stored in a `passwords.txt` file.
- **Key-based security**: A unique key is generated to encrypt and decrypt passwords.

## 🚀 How to Use

1. Run the script.
2. Choose an option:
   - **add**: Add a new account name and password. The password will be encrypted and stored.
   - **view**: View existing credentials. Encrypted passwords will be decrypted and displayed.
   - **q**: Quit the application.
3. Manage your passwords easily and securely!

## 📦 Example

```plaintext
Would you like to add a new password or view existing passwords? (add/view), or q for quit: add
Account Name: email
Password: secure123
Password saved successfully.

Would you like to add a new password or view existing passwords? (add/view), or q for quit: view
User: email | Password: secure123
```
