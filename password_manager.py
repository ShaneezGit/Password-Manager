from cryptography.fernet import Fernet
import os

# Constants for key and password file names
KEY_FILE = "key.key"
PASSWORDS_FILE = "passwords.txt"

# Generate a new Fernet encryption key
# Open key file in write-binary mode
    # Write the key to the file
def write_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)


# Check if the key file exists
    # If not, print a message to generate a new key
# Open the key file in read-binary mode
    # Read the key from the file
# Validate the key by trying tp create a Fernet object
    # If key is invalid, print a message and generate a new key
    # Re-read the key from the file
# Return the valid key   
def load_key():
    if not os.path.exists(KEY_FILE):
        print("Key file not found. Generating a new key...")
        write_key()

    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

    try:
        Fernet(key) 
    except ValueError:
        print("Invalid key detected. Generating a new key...")
        write_key()
        with open(KEY_FILE, "rb") as key_file:
            key =  key_file.read()

    return key  

# Load the encryption key and initialize the Fernet object
key = load_key()
fer = Fernet(key)


# Check if the passwords file exists
    # If not, print a message and exit the function
# Open the passwords file in read mode
    # Read each line from the file
        # Split the line into user and encrypted password
        # Decrypt the password
        # Print the user and decrypted password
        # Print an error message if the decryption fails
def view():
    if not os.path.exists(PASSWORDS_FILE):
        print("No passwords stored yet.")
        return
    
    with open(PASSWORDS_FILE, 'r') as f:
        for line in f.readlines():
            try:
                user, encrypted_pass = line.strip().split("|")
                decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
                print(f"User: {user} | Password: {decrypted_pass}")
            except Exception as e:
                print(f"Error decrypting a line: {e}")
                    

# Prompt user for account name and password
# Check if name and password is empty
    # Print a message and return if either is empty
# Encrypt the password
# Open the passwords file in append mode
    # Write the account name and encypted password to the file
# Print a success message
def add():
    name = input("Account Name: ") 
    pwd = input("Password: ")

    if not name or not pwd:
        print("Account name and password cannot be empty.")
        return
    
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open(PASSWORDS_FILE, 'a') as f:
        f.write(f"{name}|{encrypted_pwd}\n")
    print("Password added successfully.")


# Enter a coninuous loop
    # Prompt user for mode (view, add or quit)
        # Exit the loop if user chooses to quit
        # Call the view function if user chooses to view passwords
        # Call the add function if the user chooses to add a new password
        # Print an error message for invalid input
def main():
    while True:
        mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
        if mode == "q":
            break
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode. Please enter 'view', 'add' or 'q'.")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()