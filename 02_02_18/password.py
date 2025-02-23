# f(x)   -> hash
# - f()  -> this a hashing function. Creates a unique hash value for each unique
#   input. Example function sha256
# - x    -> unique information/input
# - hash -> This a fixed sized code for the hashed input

import hashlib
import password_management

# print("="*80)
# print(__file__, __name__)
# print("="*80)
password = input("Enter your password: ")
password_bytes = password.encode() # Convert the string to bytes. This is x from above
hash_bytes = hashlib.sha256(password_bytes) # Create a hash object. This is f(x) from above
hash_value = hash_bytes.hexdigest()

print("="*80)
print(hash_value)
print("="*80)

expected_hash = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
if hash_value == expected_hash:
    print("Password is correct")
else:
    print("Password is incorrect")
print("="*80)

password_management.save("admin", hash_value)
