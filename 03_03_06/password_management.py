import hashlib
from typing import Optional

RANDOM_SEQUENCE = "rvjeijbnwer"
db = [] # list of dictionaries and each dictionary is a user
# User dictionary format
# {
# "username": <value>,
# "password": < value >,
# }


def save(username: str, password: str):
    # Find existing user
    for user in db:
        if user.get("username") == username:
            user['password'] = password
            return
    
    # The user was not found in the dictionary/DB
    new_user_dict = {
        "username": username,
        "password": password
    }

    db.append(new_user_dict)
    print(db)

def load(username:str) -> Optional[str]:
    for user in db:
        if user.get("username") == username:
            return user.get("password")
    return None # Return nothing if the key (username) is not found


def sign_up():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print(f"Before hashing => {username+password[:3]+RANDOM_SEQUENCE+password[3:]}")
    password_bytes = (username+password[:3]+RANDOM_SEQUENCE+password[3:]).encode()
    hash_bytes = hashlib.sha256(password_bytes)
    hash_value = hash_bytes.hexdigest()
    save(username, hash_value)


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    expected_hash = load(username)
    if expected_hash is None: # This means the username does not exist
        print("Username and password do not match")
        return

    password_bytes = (username+password[:3]+RANDOM_SEQUENCE+password[3:]).encode()
    hash_bytes = hashlib.sha256(password_bytes)

    if hash_bytes.hexdigest() == expected_hash:
        print("Login successful")
    else:
        print("Username and password do not match")
        return

if __name__ == "__main__": # This is the entry point of the program

    # Read Event Print Loop (REPL)
    while True:
        print("="*80)
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        print("="*80)

        ui = input("Enter your choice (1, 2, or 3): ")

        # Switch exactly like else-if
        match (ui):
            case "1":
                sign_up()
            case "2":
                login()
            case "3":
                exit()
            case _:
                print("Invalid choice")
