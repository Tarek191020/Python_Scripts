from cryptography.fernet import Fernet
import os

# Function to generate a new encryption key
def Generate_key():
    key = Fernet.generate_key()
    with open("Key.txt", "wb") as Kfile:
        Kfile.write(key)
    return key

# Function to encrypt a file
def Encrypt_file(key, file_name):
    c = Fernet(key)
    with open(file_name, "rb") as file:
        data = file.read()
    encrypted_data = c.encrypt(data)
    encrypted_file_name = os.path.splitext(file_name)[0] + ".encrypted"
    extension = os.path.splitext(file_name)[1]
    with open(encrypted_file_name,"wb") as enc_file:
        enc_file.write(encrypted_data)
    os.remove(file_name)
    print(f"File '{file_name}' encrypted successfully as '{encrypted_file_name}'.")
    return encrypted_file_name

# Function to decrypt a file
def Decrypt_file(key, encrypted_file):
    d = Fernet(key)
    with open(encrypted_file, "rb") as enc_file:
        Encrypted_data = enc_file.read()
    data = d.decrypt(Encrypted_data)
    decrypted_file_name = os.path.splitext(encrypted_file)[0] + ".decrypted"
    with open(decrypted_file_name, "wb") as dec_file:
        dec_file.write(data)
    print(f"File '{encrypted_file}' decrypted successfully as '{decrypted_file_name}'.")
    
# Main program
key = Generate_key()
    
while True:
    print("operations:\n1. Encrypt a file\n2. Decrypt a file\n3. close")
    choice = input("Enter your choice: ")
        
    if choice == "1":
        file_path = input("Enter the path of the file to encrypt: ")
        Encrypt_file(key, file_path)
    elif choice == "2":
        if key:
            encrypted_file = input("Enter the path of the file to decrypt: ")
            Decrypt_file(key, encrypted_file)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")
    