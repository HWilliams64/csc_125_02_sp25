import time

# Keyword: while - condition is True, repeatedly execute the code block
# Syntax: while <condition>:
#            <code block>
# Key: If - condition is True, execute the code block
# Syntax: if <condition>:
#            <code block>

# count = 0
# while True:
#     print(f"Count: {count}")
#     count += 1 # => count = count + 1
#     time.sleep(.1)


number = int(input("Enter a number: "))
max_number = 10
while number < max_number:
    print(f"{number} is less than {max_number}")
    number += 1
