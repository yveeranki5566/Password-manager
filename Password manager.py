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


