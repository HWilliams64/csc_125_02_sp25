my_list = ["happy", "panda"] # <- used flat brackets
my_tuple = ("happy", "panda") # <- used parentheses

my_list = list(my_tuple)
my_tuple = tuple(my_list)

for item in my_tuple:
    print(item)
print("=" * 80)

print("The first item in the tuple is:", my_tuple[0])
print("The first item in the list is:", my_list[0])
