weight = float(input("Enter your weight in kilograms"))
height = float(input("Enter your height in metres"))
bmi = weight/(height**2)
print(bmi)
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi <= 25.9:
    print("normal")
elif 26 <= bmi <= 29.9:
     print("overweight")
else:
     print("Obese")


