marks = int(input("Enter Marks:"))

if 80 <= marks <= 100:
    print("You have an A")
elif 60 <= marks <= 79:
    print("You have a B")
elif 40 <= marks <= 59:
    print("You have a C")
elif 0 <= marks <= 39:
    print("You have terribly failed")
else:
    print("Wrong input")


