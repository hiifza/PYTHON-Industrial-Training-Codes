# Assignment 18 - Python Dictionary
# Name: (Write your name here)

print("----- Question 1 -----")
# 1. Create and print a dictionary storing your information
my_info = {
    "name": "Hifza Amir",
    "age": 21,
    "gender": "Female",
    "course": "CSE"
}
print(my_info)


print("\n----- Question 2 -----")
# 2. Access dictionary items using key
print("Name:", my_info["name"])
print("Age:", my_info["age"])


print("\n----- Question 3 -----")
# 3. Get list of values from dictionary
values = list(my_info.values())
print("Values:", values)


print("\n----- Question 4 -----")
# 4. Change value of a specific item using key
my_info["age"] = 22
print("Updated dictionary:", my_info)


print("\n----- Question 5 -----")
# 5. Print all key names one by one
print("Keys:")
for key in my_info.keys():
    print(key)


print("\n----- Question 6 -----")
# 6. Create a dictionary containing three dictionaries (nested)
students = {
    "student1": {"name": "Abc", "age": 20},
    "student2": {"name": "Def", "age": 21},
    "student3": {"name": "Ghi", "age": 22}
}
print(students)


print("\n----- Question 7 -----")
# 7. Create three dictionaries, then one dictionary containing them
dict1 = {"a": 1}
dict2 = {"b": 2}
dict3 = {"c": 3}

combined_dict = {
    "dict1": dict1,
    "dict2": dict2,
    "dict3": dict3
}
print(combined_dict)


print("\n----- Question 8 -----")
# 8. Convert two lists into a dictionary
list1 = ["name", "age", "gender"]
list2 = ["Hifza", 21, "Female"]

converted_dict = dict(zip(list1, list2))
print(converted_dict)


print("\n----- Question 9 -----")
# 9. Merge two dictionaries
dict_a = {"x": 10, "y": 20}
dict_b = {"z": 30}

merged_dict = dict_a | dict_b   # Python 3.9+
print(merged_dict)


print("\n----- Question 10 -----")
# 10. Get key of lowest value from dictionary
sample_dict = {
    "C": 92,
    "Java": 66,
    "Python": 85
}

lowest_key = min(sample_dict, key=sample_dict.get)
print("Key with lowest value:", lowest_key)
