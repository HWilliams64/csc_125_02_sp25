import hashlib

# print("="*80)
# print(__file__, __name__)
RANDOM_SEQUENCE = "rvjeijbnwer"

def save(key:str, value:str):
    with open("passwords.txt", "a") as file:
        file.write(f"{key} {value}\n")

def load(key:str) -> str:
    with open("passwords.txt", "r") as file:
        for line in file:
            k, v = line.split()
            if k == key:
                return v
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

        # if ui == "1":
        #     sign_up()
        # elif ui == "2":
        #     login()
        # elif ui == "3":
        #     exit()
        # else:
        #     print("Invalid choice")

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
