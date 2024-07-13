# Taking input for height and weight and converting them to floats
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# Calculating BMI
bmi = round(weight / height ** 2)

# Printing BMI and corresponding category
if bmi < 18.5:
    print(f"Your BMI is {bmi}, and you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, and you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, and you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, and you are obese.")
else:
    print(f"Your BMI is {bmi}, and you are clinically obese.")
