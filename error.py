try:
    num = int(input("Enter a number :- "))
    print(num)
    c = 10 / num
except ValueError as e:
    print("Value Error")
except ZeroDivisionError as e:
    print(e)
else:
    print(c)
print("Tasin Coder")