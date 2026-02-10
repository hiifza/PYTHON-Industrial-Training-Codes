# Assignment: Python Strings
# All questions solved correctly in one file

print("PYTHON STRING ASSIGNMENT")
print("=" * 30)

# 1. Create a string in 3 different ways
print("\n1. Creating strings in 3 different ways:")
s1 = "TasinCoder"
s2 = 'TasinCoder'
s3 = str("TasinCoder")

print(s1)
print(s2)
print(s3)

# 2. Get characters from start to position 5 (TasinCoder)
# (Position means index-based slicing: 0 to 4)
print("\n2. Characters from start to position 5:")
s = "TasinCoder"
print(s[0:5])

# 3. Get characters from position 2 to position 5 (Hello Learners)
print("\n3. Characters from position 2 to position 5:")
s4 = "Hello Learners"
print(s4[2:5])

# 4. Concatenate two strings with space
print("\n4. String Concatenation:")
a = "Learning"
b = "Python"
print(a + " " + b)

# 5. Count total number of characters in "TasinCoder"
print("\n5. Total number of characters:")
print(len("TasinCoder"))

# 6. Reverse a string
print("\n6. Reverse the string:")
print("TasinCoder"[::-1])

# 7. Check whether string contains a substring
print("\n7. Check substring:")
main_string = "Python is powerful"
sub_string = "powerful"

if sub_string in main_string:
    print("Substring found")
else:
    print("Substring not found")

# 8. Check if string contains only numbers
print("\n8. Check if string contains only numbers:")
num_str = "12345"

if num_str.isdigit():
    print("Only numbers")
else:
    print("Not only numbers")

# 9. Check if string contains only alphabets
print("\n9. Check if string contains only alphabets:")
alpha_str = "Python"

if alpha_str.isalpha():
    print("Only alphabets")
else:
    print("Not only alphabets")

# 10. Convert integer to string
print("\n10. Convert integer to string:")
x = 50
y = str(x)
print(y)
print(type(y))

print("\nASSIGNMENT COMPLETED SUCCESSFULLY")
