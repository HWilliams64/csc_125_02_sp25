# Keyword for - iterate over a sequence of elements
# Syntax: for <element> in <sequence>:
#            <code block>

# my_string = "Hello my name is Harris how are you?"

# for char in my_string:
#     if char == " ":
#         continue
#     if char == "n":
#         break
#     print(char)

start = 1
stop = 10
step = 2
for i in range(start, stop+1, step):
    print(i)


print("panda" in "happy pandas")
