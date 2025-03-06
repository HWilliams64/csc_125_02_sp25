license_dict = {
    "iss": "03/04/2025",
    "number": "S1234556",
    "exp": "03/04/2026",
    "dob": "03/04/2000",
    "first_name": "Marshall",
    "last_name": "Mathers",
}


first = license_dict["first_name"]
last = license_dict["last_name"]

print(f"Full name: {first} {last}")


# Set a value
license_dict["first_name"] = "Tony"
license_dict["last_name"] = "Stark"

first = license_dict["first_name"]
last = license_dict["last_name"]

print(f"Full name: {first} {last}")

# Add a key value
license_dict["state"] = "NY"
state = license_dict["state"]
print(f"{first} {last} is from {state}")

print(license_dict)

# Remove 
# The value must be in the dict
# del license_dict["state"]
# This returns the value to be removed
old_value = license_dict.pop("state")
print(license_dict)
license_dict["state"] = old_value

# Getting a value

# Check if middle name in dict before attempting to get it 
if "middle_name" in license_dict:
    middle_name = license_dict["middle_name"]
else:
    middle_name = ""

middle_name = license_dict.get("middle_name", " ")
if middle_name != " ":
    middle_name = " "+middle_name+" "

print(f"{first}{middle_name}{last}")

# state = license_dict["state"]


# my_list = [1, 2, 3]
# my_list[100]

print("="*80)
for key in license_dict:
    print(key, ":", license_dict[key])

print("="*80)
for value in license_dict.values():
    print(value)

print("="*80)
for key, value in license_dict.items():
    print(key, ":", value)

print("="*80)
s3 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for x, y, z in s3:
    print("x:", x, "y:", y, "z:", z)
print("0, 0 =", s3[1][0])