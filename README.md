# Password-manager

Created a simple password manager with a graphical user interface (GUI) using Tkinter, which is a standard GUI library for Python. The password manager will be able to securely store credentials for different accounts.
The passwords are encrypted using Fernet which is a part of cryptography library. The two major functions of this password manager is to encrypt and save new passords to each user and to retrieve the decrypted password when needed. 

## Step by Step implementation of the python program

1. First we import the required modules and libraries such as tkinter, message and fernet from the cryptography package.
2. Next we will define functions for generating key, encryption and for decryption of the entered password.

When encrypt_password is provided with a key and a password, it encrypts the password and produces an encrypted password as a string. Similarly, decrypt_password uses the key and the encrypted password to decode it and return the original password as a string.

<img width="254" alt="image" src="https://github.com/user-attachments/assets/d7b52e4a-f792-4984-a79e-e8059ceeab16">

3. Create a dictionary to store passwords.
4. To include new passwords in the dictionary, the add_password function will be used. To access a password from the dictionary, the get_password function is used. This function retrieves the password associated with the provided Account Name and shows the decrypted password using a message box.
5. Using grids and the geometry manager, Tkinter allows us to design a user-friendly interface for our Password Manager.
6. After entering the details, clicking the “Add Password” button activates the add_password function, which saves the encrypted data to the dictionary. Upon completion, the code will confirm the successful operation with a message box notification.

<img width="272" alt="image" src="https://github.com/user-attachments/assets/e47b515d-e1da-4a34-860c-170b92318a78">

7. To access a stored password, the user should enter the Service/Account name into the input box and click the “Get Password” button. This action triggers the get_password function to retrieve and decrypt the requested password. Once completed, the password will be shown to the user in a message box.

<img width="290" alt="image" src="https://github.com/user-attachments/assets/10ab90d0-bf70-4644-85f1-852b335198e8">

## Source code

```
import tkinter
from tkinter import messagebox
from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()
def encrypt_password(key, password):
    cipher = Fernet(key)
    return cipher.encrypt(password.encode()).decode()
def decrypt_password(key, encrypted_password):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_password.encode()).decode()


passwords = {}

# Function to add a password
def add_password():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if service and username and password:
        encrypted_password = encrypt_password(key, password)
        passwords[service] = {'username': username, 'password': encrypted_password}
        messagebox.showinfo("Success", "Password added!")
        service_entry.delete(0, tkinter.END)
        username_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)
    else:
        messagebox.showwarning("Error", "Enter all the fields.")

# Function to view passwords
def get_password():
    service = service_entry.get()
    if service in passwords:
        encrypted_password = passwords[service]['password']
        decrypted_password = decrypt_password(key, encrypted_password)
        messagebox.showinfo("Password", f"Username: {passwords[service]['username']}\nPassword: {decrypted_password}")
    else:
        messagebox.showwarning("Error", "Password not found.")


key = generate_key()

# Create the main window
root = tkinter.Tk()
root.title("Password Manager")

# Create and place widgets
tkinter.Label(root, text="Account").grid(row=0)
tkinter.Label(root, text="Username").grid(row=1)
tkinter.Label(root, text="Password").grid(row=2)

service_entry = tkinter.Entry(root)
username_entry = tkinter.Entry(root)
password_entry = tkinter.Entry(root, show='*')  # Hide password input

service_entry.grid(row=0, column=1)
username_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)

tkinter.Button(root, text="Add Password", command=add_password).grid(row=10, column=4, columnspan=4)
tkinter.Button(root, text="View Passwords", command=get_password).grid(row=12, column=4, columnspan=4)

root.mainloop()

```





