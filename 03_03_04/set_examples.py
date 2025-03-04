my_set = {"Happy", "pandas", "dance", "in", "the", "moon", "light", "dance", "in", "the", "moon", "light"}
print("Original set:", my_set)
print("Original set:", my_set)

# ❌ my_set[0] <= indexing is not supported

# Access
removed_item = my_set.pop()
print("Popped item:", removed_item)
print("After pop():", my_set)

# Add and remove
my_set.add(removed_item)
print("After add():", my_set)

# my_set.clear()
my_set.remove("in")
print("After remove():", my_set)
my_set.add("in")
print("After add():", my_set)

intro_students = {"a", "b", "c", "f", "g", "h"}
adv_students = {"a", "b", "c", "d", "e"}

overlapping_students = 0
for intro_student in intro_students:
    for adv_student in adv_students:
        if intro_student == adv_student:
            overlapping_students += 1
print("Number of overlapping students:", overlapping_students)

overlapping_students = intro_students.intersection("abcd")
print("Number of overlapping students:", len(overlapping_students))

non_overlapping_students = intro_students.difference(adv_students)
print("Non-overlapping students:", non_overlapping_students)


print(adv_students.issubset(intro_students))
